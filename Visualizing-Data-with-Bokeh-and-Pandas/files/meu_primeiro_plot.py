# meu_primeiro_plot.py

from bokeh.plotting import figure, output_file, show

output_file('meu_primeiro_grafico.html')

x = [1, 3, 5, 7]
y = [2, 4, 6, 8]

p = figure()

p.circle(x, y, size=10, color='red', legend='círculo')
p.line(x, y, color='blue', legend='linha')
p.triangle(y, x, color='gold', size=10, legend='triângulo')

p.legend.click_policy='hide'

show(p)