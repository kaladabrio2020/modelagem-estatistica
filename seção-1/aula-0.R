
set.seed(10)
x = rnorm(10)
y = x + x*2 + 0.3

plot(x, y, pch=19)

# criando modelo no R
model_ = lm(y~x)

# Imprimindo o R
model_


# Sumario
summary(model_)

p
