# import les librairies necessaires
import pandas as pd
import statsmodels.api as sm

# load the data
df = pd.read_excel('Donnees_Exercice_4_2.xlsx')
# print the data
print(df)

# print a description of the data
print(df.describe())

# print all column names
print(df.columns)

# add a new column to the data frame (visites par personne)
df["Visits_per_person"] = df["Visits "] / df["Population"]
# reprint de data frame
print(df)

# ces variables viennent de lenonce de la question 4.2 donc on fais juste les assigner
Dry_revenu = 31500
Dry_population = 70230

#premiere methode de regression que le prof donne:
#Visits_per_person = alpha_0 + alpha_1 * Fee + alpha_2 * Income
#on assigne alors les variables Fee et Income a X et Visits_per_person a y
X = df[['Fee ($)', 'Income ($)']]
X = sm.add_constant(X)
y = df['Visits_per_person']

#on regresse les variables
model = sm.OLS(y, X).fit()

#on recupere les coefficients
coefficients = model.params

#on calcule alpha_0 et alpha_1
alpha_0 = (coefficients['const'] + coefficients['Income ($)'] * Dry_revenu) * Dry_population
alpha_1 = coefficients['Fee ($)'] * Dry_population

#on les affiches
print(f"alpha_0: {alpha_0}")
print(f"alpha_1: {alpha_1}")

#on calcule q et on le print
q1 = alpha_0 + alpha_1
print(f"q1: {q1}")

#on fait la seconde regression avec les variables Fee, Income et Population comme variables explicatives
#et simplement Visits comme variable a predire. ca fait du sens puisque dans un cas, tu utilise une variable qui
#deja un ratio de visites par personne et dans l'autre tu utilise directement le nombre de visites mais
#on rajoute la population dans les variables expliquatives.
#on peut dire que c'est equivalent
X = df[['Fee ($)', 'Income ($)', "Population"]]
X = sm.add_constant(X)
y = df['Visits ']

#on roule la deuxieme regression
model = sm.OLS(y, X).fit()

#on recupere encore les coeficients
coefficients = model.params

#on calcule alpha_0 et alpha_1 puis on les imprime
alpha_0 = (coefficients['const'] + coefficients['Income ($)'] * Dry_revenu + coefficients['Population'] * Dry_population)
alpha_1 = coefficients['Fee ($)']

print(f"alpha_0: {alpha_0}")
print(f"alpha_1: {alpha_1}")

#on calcule q2 et on le print
q2 = alpha_0 + alpha_1

print(f"q2: {q2}")


# a) with regression 2

p_bar = -1*alpha_0/alpha_1
print(f"p_bar: {p_bar}")

CS = 0.5 * p_bar * alpha_0

print(f"CS: {CS}")


# b) with regression 2

p1 = 1
q1 = alpha_0 + alpha_1 * p1
CS = 0.5 * (p_bar - p1) * q1

METB = 0.25

b = CS + p1 * q1 * 1 + METB

print(f"q1: {q1}")
print(f"CS: {CS}")
print(f"b: {b}")


# results
'''
    Town  Visits   Fee ($)  Income ($)  Population
0      1   168590     0.00       20600       36879
1      2   179599     0.00       33400       64520
2      3   198595     0.00       39700      104123
3      4   206662     0.00       32600      103073
4      5   170259     0.00       24900       58386
5      6   209995     0.25       38000      116592
6      7   172018     0.25       26700       49945
7      8   190802     0.25       20800       79789
8      9   197019     0.25       26300       98234
9     10   186515     0.50       35600       71762
10    11   152679     0.50       38900       40178
11    12   137413     0.50       21700       22928
12    13   158056     0.50       37900       39031
13    14   157424     0.50       35100       44685
14    15   179490     0.50       35700       67882
15    16   164657     0.75       22900       69625
16    17   184428     0.75       38600       98408
17    18   183822     0.75       20500       93429
18    19   174510     1.00       39300       98077
19    20   187820     1.00       25800      104068
20    21   196318     1.25       23800      117940
21    22   166694     1.50       34000       59757
22    23   161716     1.50       29600       88305
23    24   167505     2.00       33800       84102
            Town        Visits     Fee ($)    Income ($)     Population
count  24.000000      24.000000  24.000000     24.000000      24.000000
mean   12.500000  177191.083333   0.604167  30675.000000   75488.250000
std     7.071068   17877.524342   0.541318   6843.673689   27360.701213
min     1.000000  137413.000000   0.000000  20500.000000   22928.000000
25%     6.750000  166184.750000   0.250000  24625.000000   56275.750000
50%    12.500000  177000.000000   0.500000  33000.000000   75775.500000
75%    18.250000  188565.500000   0.812500  36250.000000   98277.500000
max    24.000000  209995.000000   2.000000  39700.000000  117940.000000
Index(['Town', 'Visits ', 'Fee ($)', 'Income ($)', 'Population'], dtype='object')
    Town  Visits   Fee ($)  Income ($)  Population  Visits_per_person
0      1   168590     0.00       20600       36879           4.571436
1      2   179599     0.00       33400       64520           2.783617
2      3   198595     0.00       39700      104123           1.907312
3      4   206662     0.00       32600      103073           2.005006
4      5   170259     0.00       24900       58386           2.916093
5      6   209995     0.25       38000      116592           1.801110
6      7   172018     0.25       26700       49945           3.444149
7      8   190802     0.25       20800       79789           2.391332
8      9   197019     0.25       26300       98234           2.005609
9     10   186515     0.50       35600       71762           2.599078
10    11   152679     0.50       38900       40178           3.800065
11    12   137413     0.50       21700       22928           5.993240
12    13   158056     0.50       37900       39031           4.049499
13    14   157424     0.50       35100       44685           3.522972
14    15   179490     0.50       35700       67882           2.644147
15    16   164657     0.75       22900       69625           2.364912
16    17   184428     0.75       38600       98408           1.874116
17    18   183822     0.75       20500       93429           1.967505
18    19   174510     1.00       39300       98077           1.779316
19    20   187820     1.00       25800      104068           1.804781
20    21   196318     1.25       23800      117940           1.664558
21    22   166694     1.50       34000       59757           2.789531
22    23   161716     1.50       29600       88305           1.831335
23    24   167505     2.00       33800       84102           1.991689
alpha_0: 211515.02715381465
alpha_1: -40420.69803036392
q1: 171094.32912345073
alpha_0: 182863.19559795945
alpha_1: -14638.574021567285
q2: 168224.62157639215
p_bar: 12.491872181576134
CS: 1142151.8330621326
q1: 168224.62157639215
CS: 966607.9244749567
b: 1134832.7960513488
'''