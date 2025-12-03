library(ggplot2)  # For plotting
library(stats)  # For linear regression

# Read the CSV file
df <- read.csv("exam_dataset.csv")

# Print summary statistics
cat("\nSummary statistics:\n")
print(summary(df))

if (is.character(df$Gender) || is.factor(df$Gender)) {
  df$Gender <- ifelse(df$Gender == "Female", 0, 1)
}

cat("\nUpdated 'Gender' column values:\n")
print(table(df$Gender))

X <- df[, c("HoursStudied", "PreviousScore", "ParentalInvolvement", "Gender")]
y <- df$ExamScore

# Run multiple linear regression
model <- lm(y ~ ., data = X)

# Get and print the OLS Regression Summary
cat("\nRegression Summary:\n")
regression_summary <- summary(model)
print(regression_summary)

cat("R-squared:\n")
print(regression_summary$r.squared)  # Multiple R-squared

cat("\nAdjusted R-squared:\n")
print(regression_summary$adj.r.squared)  # Adjusted R-squared

cat("\nF-statistic:\n")
print(regression_summary$fstatistic)  # F-statistic details


# Visualization 1: Previous Score vs Exam Score
ggplot(df, aes(x = PreviousScore, y = ExamScore)) +
  geom_point(color = "blue") +
  labs(x = "\nPrevious Score", y = "Exam Score", title = "\nPrevious Score vs Exam Score\n") +
  theme_minimal() +
  theme(panel.grid.major = element_line(color = "black", linetype = "dashed"))

# Visualization 2: Actual vs Predicted Exam Scores
pred <- predict(model, X)

ggplot(data.frame(Actual = df$ExamScore, Predicted = pred), aes(x = Actual, y = Predicted)) +
  geom_point(color = "blue") +
  geom_abline(intercept = 0, slope = 1, color = "red", linetype = "dashed") +
  labs(x = "Actual Exam Score", y = "Predicted Exam Score", title = "\nActual vs Predicted Exam Scores\n") +
  xlim(min(df$ExamScore), max(df$ExamScore)) +
  ylim(min(pred), max(pred)) +
  theme_minimal() +
  theme(panel.grid.major = element_line(color = "black", linetype = "dashed"))
