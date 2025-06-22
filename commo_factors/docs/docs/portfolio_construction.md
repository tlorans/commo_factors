# How to Construct a Multi-Factor Commodity Portfolio?

- Explain portfolio theory in the context of multiple factors 
- Show how to build an optimal commodity portfolio
- Static (equal-weight or risk-parity) vs. optimized weighting 
- Implementation challenges 

(part 5. of the paper, multifactor commodity portfolios)

## Equally-Weighted Commodity Factor Portfolio 

The equally weighted commodity factor portfolio investes proportionally in each of the three commodity factors and since it does not use estimates of return or risk, is by definition free of estimation risk. EW will be mean-variance optimal when commodity factor expected returns, variances and correlations are the same. 


## The Inverse Variance Portfolio

The inverse variance (IV) portfolio rule depends only on variance and assumes that the correlation between the factors is zero. IV weights are calculated according to the following equation:

$$
w_{i,t} = \frac{1/\sigma_{i,t}^2}{\sum_{j=1}^{N} 1/\sigma_{j,t}^2}
$$ 

where \\(\sigma_{i,t}^2\\) is the estimated variance of commodity \\(i\\). 

## MinVar Rule 

MinVar rule is the short sale-constrained minimum variance portfolio of commodity factors. 