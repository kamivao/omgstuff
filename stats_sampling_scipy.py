import scipy as sp
import numpy as np
import sklearn
import scipy.stats as stats

a = [26.77, 25.77, 25.95, 26.18, 27.25, 28.19, 26.24, 28.29, 25.28, 29.51, 27.42, 26.18, 26.69, 22.73, 23.77, 25.57, 26.8, 26.9, 24.27, 27.92]
array_length = len(a)
print(array_length)
sum = np.sum(a, dtype=np.float64)
print(sum)
avg_param = sum/array_length
print(avg_param)


sample_array = [17.4, 19.9, 19.9, 19.0, 20.7, 18.2, 18.6, 20.3, 21.7, 20.8, 16.7, 20.3, 22.5, 18.3, 21.1, 16.3, 22.0, 19.5, 18.1, 21.1, 20.0, 21.6, 21.5, 21.1, 23.3, 23.0, 17.8, 19.5, 21.6, 22.9]
array_length_2 = len(sample_array)
print(array_length_2)
sum_2 = np.sum(sample_array, dtype=np.float64)

sum_of_squared_values = 0

for each in sample_array:
    sq = np.power(each, 2)
    sum_of_squared_values += sq
variance_estim = sum_of_squared_values/array_length_2
print("var estim = %f" %variance_estim)
print("sum of squared values =  %f" %sum_of_squared_values)

variance = np.var(sample_array)
print("variance (valid) = %f" %variance)

#Задача из С.Гланца, с.97 (о больных пиелонефритом)

n1 = n2 = 36

avg_right_treatment = 4.51
avg_wrong_treatment = 6.28

sigma_right_treatment = 1.98
sigma_wrong_treatment = 2.54

#df - степени свободы, n1+n2-2
df = n1+n2-2
print("степени свободы df = %d" %df)

t = (avg_right_treatment - avg_wrong_treatment)/np.sqrt(np.power(sigma_right_treatment,2)/n1 + np.power(sigma_wrong_treatment,2)/n2)
print("значение t = %f" %t)


#сгенерируем две выборки с параметрами матожидание, стандартное отклонение, размер
#https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.normal.html
#s = np.random.normal(mu, sigma, 1000)
sample_right_treatment = np.random.normal(avg_right_treatment, sigma_right_treatment, 36)
sample_wrong_treatment = np.random.normal(avg_wrong_treatment, sigma_wrong_treatment, 36)

#equal_var = False, если разные дисперсии
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html
t_value, p_value = stats.ttest_ind(sample_right_treatment,sample_wrong_treatment)
print(t_value, p_value)