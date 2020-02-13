# Create Dummy Experimental Data 

baseline <- rnorm(n = 132, mean = 5.45,sd = 2)
experiment <- rnorm(n = 132, mean = 8.76,sd = 2)

df <- data.frame(baseline, experiment)

write.csv(df, file = "experiment_data.csv")

t.test(df$baseline, df$experiment, var.equal = FALSE)
