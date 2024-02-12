### Notes

* Add an application of multinomial logistic regression / LDA / QDA, etc.

### sklearn
* Use `cross_val_score` for cross-validation.
* Or GridSearch.

* Maybe power transforms instead of log transforms?


### ISLP
* No, just use `sklearn.feature_selection.SequentialFeatureSelector` instead. Make short note about `SequentialFeatureSelector`.

#### Drop
* `GAM`
* `PLS`
* Smoothing splines
* Local regression
* Bootstrap
* Generalized linear models


### statsmodels
* Avoid this one too; use sklearn only.


### Rough plan
1. Use almost exclusively the ISLP book, ch. 1 - 7. (Or 1 - 6.)
  * Pros:
    * Has excellent reviews.
    * Uses Python already.
    * Has "lab" section only focused on applications. 
    * Is focused on applications.
    * Most famous book.
    * Good exercises.
    * Written by very important people.
    * Several exercises online that are inline with the book.
    * Not very mathematically sophisticated.
    * Uses sklearn instead of statsmodels.
  * Cons:
    * Too large chapters, so I need to split up exercises.
    * Too large chapters might make it necessary to give asymmetric reading
      assignments.
    * Uses the package ISLP when scklearn and statsmodels + patsy would have 
      sufficed.
2. Use Jan's approach with combined lecture and exercise solving. Ask to read
   the book before the lecture?
3. Change course name to e.g. Statistical learning. 
4. Make mock exam during the summer.
5. Interleaved exercises.
6. 5 min recap each lecture.
7. 3-hour sessions?
7. Please read the chapters before coming to class.
7. Lectures, book, and *exercise solutions* are on the curriculum.
8. Use plans + website for the exercise solutions and extra notes (kept at a minimum.)
8. Two exams: One home project (week) and one conceptual (2 hours?).
8. Conceptual flash cards? (Write while reading through book.) (Should not take too long.)
9. Write solutions to programming exercises in Jupyter Notebooks or Quarto.
10. Accept Quarto or Jupyter notebooks on project exam.
10. https://erictleung.com/pyblack-rstudio-addin
11. Consider adding snipets from the user-guide to `sklearn` as curriculum.
12. Title: Data Science with sklearn and Python


11. Remember to read through all exercise solutions; I will learn a lot while solving them.


Recap (probability, numerics), 1,2,3,4 (except 4.6 on GLM), 5 (maybe need a note on bootstrap), 6, 7 (except 7.7?)




**Recommend to save all exercises in their separate file, e.g., a Jupyter
Notebook. We often split exercises over several sessions.**

**Please read the chapters before coming to class.**

**Make sure the exercises match the problems.**

01. Recap lecture: Probability and statistics
  * Curriculum.
    * PDF, CDF, etc.
    * Scientific notation.
    * Conditional expectation
    * Covariance and correlation.
    * Scatter plots
    * Common distributions: Poisson distribution, normal distribution, etc.
    * How to simulate from these and plot histograms.
    * All of this is on the curriculum, and is needed for the remainder.
02. Recap lecture: Programming and Numpy
  * Curriculum.
    * Looping. Pythonic code.
    * Dictionaries and dictionary comprehensions.
    * Working with Numpy.
    * Statistical simulation
    * Scitkit learn (sklearn).
  * Exercises.
    * 
03. Introduction & Statistical Learning
  * The whole chapters as curriculum.
    * Training set and test set.
    
  * **Exercises.** 
    * All conceptual ones. (+ interleaving)
    * All applied ones: One in class, one as homework? 
04. Linear regression (i): Definition and estimation
  * 3.1, 3.2.1, 3.6.1 - 3.6.3 (slightly more details in the lecture itself, including implementation in Numpy.)
  * **Custom exercises:**
    * (i) Verify the linear regression equations. 
    * (ii) Questions about interpretation.
  * **Exercises from the book.**
05. Linear regression (ii): Model selection and k-nearest neighbors
  * 3.2.2, 3.5, 3.6.4
  * **Exercises:**
    * 
    * 
06. Linear regression (iii): Model selection
  * 3.3 - 3.4, 3.6.5 - 3.6.7
  * One-hot-encoding.
    * Basic usage of `sklearn.compose`'s ColumnTransformer.
    * Done automatically by `statsmodels`.
  * **Exercises:**
07. Classification (i): Logistic regression
  * 4.1 - 4.3, Lab: 4.7.1 - 4.7.2
  * **Exercises:**
    * **Conceptual.**
      * 4.8.1, 4.8.6, 4.8.8 (?), 4.8.9, 4.8.12, 8.4.4 (additional exercise)
    * **Programming.**
      * 4.8.13(a-d), 4.8.14(a-c,f), 4.8.15, 4.8.16 (using logistic regression)
08. Classification (ii): Discriminant analysis and naïve Bayes
  * 4.4 - 4.6, Lab: 4.7.3 - 4.7.6
  * **Exercises:**
    * **Conceptual.**
      * 4.8.2, 4.8.3, 4.8.5, 4.8.7,
    * **Programming.**
      * 4.8.13(e-j), 4.8.15(d-e, g-h), 4.8.16 (with all methods)
09. Resampling methods: Cross-validation and bootstrap
  * Crossvalidation using pipelines.
  * https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation
  * 5.1 - 5.3
  * **Exercises:**
    * **Conceptul.**
      * 5.4.1, 5.4.2, 5.4.3, 
    * **Programming.**
      * 5.4.5 - 5.4.9.
10. Linear Model Selection and Regularization (i): Ridge regression and LASSO
  * One part ridge, one part LASSO.
  * One addititional part with pipelines and scalers in `sklearn`. (+ exercises.)
  * https://scikit-learn.org/stable/common_pitfalls.html
  * 6.1 - 6.2, Lab: 6.5.1 - 6.5.2
  * **Exercises:**
    * **Conceptul.**
      * 6.6.1, 6.6.2(a-b), 6.6.3, 6.6.4, 6.6.6, 
    * **Programming.**
      * 6.6.8, 6.6.9(a-d), 6.6.10, 
11. Linear Model Selection and Regularization (ii): Principal component analysis
  * One part PCA, one part considerations. (Potentially with more )
  * The part about PCA is weak.
  * 6.3.1, 6.4, Lab: 6.5.3
  * Content: PCA considerations
  * **Exercises:**
    * **Conceptual.**
      * (Here there are many possible questions - maybe add one or two.)
    * **Applications**
      * 6.6.8, 6.6.9(e-g), 6.6.11
12. Moving Beyond Linearity (i): Polynomials and splines
  * One part about pipelines and transformations.
    * PolynomialFeatures
    * SplineTransformer
    * KBinsDiscretizer
  * 7.1 - 7.5, Lab: 7.8.1 - 7.8.2
  * Content:
    * Polynomials, step functions, splines.
    * Optional reading: Bernstein polynomials.
    * Optional reading: Monotone splines.
  * **Exercises:**
    * **Conceptual.**
      * 7.9.2, 7.9.3, 7.9.4, 7.9.5, 7.9.9 ((a) use PolynomialFeatures, not `poly`; (d) use SplineTransformer, not `bs`)
    * **Applications**
      * 7.9.6, 7.9.7 (using spline methods), 7.9.9, (Add one or two more, maybe.)
13. Moving Beyond Linearity (ii): Local regression and generalized additive models
  * 7.6 (skip the question about ANOVA) - 7.7; Lab: 7.8.3 - 7.8.4
  * **Content:**
    * Local regression and generalized additive models.
  * **Exercises:**
    * 6.6.2(c), 7.9.7, 7.9.8, 7.9.10, 7.9.11, 7.9.12
14. Tree-based methods
  * 8
  * Comments:
    * Use CAT boost or something similar. 
  * **Content:**
    * Local regression and generalized additive models.
  * **Exercises:**
    * 8.4.4, 8.4.5, 8.4.6, 8.4.7
15. Summing up and exam review
  * Summing up.
  


08. AB-testing
09. Interlude on Numpy
10. Statistical simulation
11. Some important univariate statistical models
12. Sample statistics and heavy tails
13. Maximum likelihood and the central limit theorem
14. Exploratory data analysis
15. Recap
