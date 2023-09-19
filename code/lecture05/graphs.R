y <- seq(0.001, 0.999, 0.001)
x <- seq(-3, 3, by = 0.01)

plot(x, pnorm(x), xlab = "p", ylab = "x", type = "l", main = "Cumulative distribution function", lwd = 2)
plot(y, qnorm(y), xlab = "x", ylab = "p", type = "l", main = "Quantile function", lwd = 2)
