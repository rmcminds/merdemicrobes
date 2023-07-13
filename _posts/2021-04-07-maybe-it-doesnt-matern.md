---
layout: post
title: "Maybe it doesn't Matern"
date: 2021-04-07
categories: code
tags:
- code
- Stan
- stats
---
Calling all bored and crazy Stan coders. I need a long term coding partner.

I’ve been doing a lot of completely solo work for a couple years now, and you can guess the result. I have a couple of really awesome models that I am proud of, and yet they’re (1) not quite what I want, (2) probably way more complicated and messy than necessary, and (3) sitting there, waiting for me to figure out how to be a real modeler and justify them.

One of the things I was recently working on and am a bit stuck on is a Stan implementation of the circular Matern covariance function as described in “Covariance functions for mean square differentiable processes on spheres” (Guinness & Fuentes 2013). I just learned that the quadratic exponential covariance that I had been using is technically not valid for spherical distances, and that the linear exponential covariance is non-differentiable (bad for parameters in Stan, yes?). So this would be a nice addition. And I’m pretty sure I translated the math correctly, but it doesn’t… work. A few iterations of ADVI and it diverges when using my circular Matern implementation, whereas the version of my model with the technically invalid quadratic exponential runs just fine. So maybe I’m trying to solve a problem that doesn’t exist – but I want to make it work anyway!

Here’s the code I’ve got. I’ve filtered out a bunch of unnecessary details but haven’t cleaned the remainder up…

```
functions {
    real ff(int k, int j) {
        if(j)
          return(falling_factorial(k,j));
        else
          return(1);
    }
    vector circular_matern(vector d, int n, real alpha, matrix ffKJ, matrix chooseRJ) {
        real ap = alpha * pi();
        row_vector[2] csap = [cosh(ap), sinh(ap)];
        matrix[n-1,n] H;
        real annm1 = inv((-2 * square(alpha))^(n-1) * tgamma(n));
        vector[n] a;
        vector[rows(d)] adp = alpha * (d-pi());
        matrix[rows(d),2] csadp = append_col(cosh(adp), sinh(adp));
        vector[rows(d)] cov = zeros_vector(rows(d));
        for(k in 0:(n-1)) {
          for(r in 0:(n-2)) {
            H[r+1,k+1] = 0;
            for(j in 0:(2*r+1)) {
              if(j <= k) {
                H[r+1,k+1]
                 += chooseRJ[r+1,j+1]
                    * ffKJ[k+1,j+1]
                    * ap^(k-j)
                    * csap[((k-j+1) % 2) + 1];
              }
            }
          }
        }
        a = append_row(-annm1 * (H[,1:(n-1)] \ H[,n-1]), annm1);
        for(k in 0:(n-1)) {
          cov += a[k+1] * adp^k .* csadp[,(k % 2) + 1];
        }
        return(cov / (2*alpha*csap[2]));
    }
    matrix fill_sym(vector lt, int N, real c) {
        matrix[N,N] s_mat;
        int iter = 1;
        for(j in 1:(N-1)) {
            s_mat[j,j] = c;
            for(i in (j+1):N) {
                s_mat[i,j] = lt[iter];
                s_mat[j,i] = lt[iter];
                iter += 1;
            }
        }
        s_mat[N,N] = c;
        return(s_mat);
    }
}
data {
    int M[DRC];
    vector[choose(M[size(M)],2)] distSites; // distm(latlon)[lower.tri(distm(latlon)]
    int ms; // Matern smoothness parameter
}
transformed data {
    matrix[ms-1, 2 * ms] chooseRJ;
    matrix[ms, 2 * ms] ffKJ;
}
parameters {
    matrix<lower=0>[DRC+D,K] weight_scales;
    vector<lower=0>[K] siteDecay; //alpha
    vector<lower=0, upper=1>[K] siteProp; //nugget
}
transformed parameters {
    for(k in 1:K) {
        covSites[k]
            = fill_sym(siteProp[k]
                       * square(weight_scales[DRC,k])
                       * circular_matern(distSites, ms, inv(siteDecay[k]), ffKJ, chooseRJ),
                       M[size(M)],
                       square(weight_scales[DRC,k]) + 1e-10);
        // below is the alternative, which works
        //covSites[k]
        //    = fill_sym(siteProp[k]
        //               * square(weight_scales[DRC,k])
        //               * exp(-square(distSites) / (2 * square(siteDecay[k]))),
        //               M[size(M)],
        //               square(weight_scales[DRC,k]) + 1e-10);
    }
}
model {
    weight_scales ~ student_t(2,0,2.5);
    siteDecay ~ inv_gamma(5,5);
}
```
