import pygal

def generate_system_usage_chart():
    line_chart = pygal.Line()
    line_chart.title = 'System Performance Metrics over time (in minutes) '
    line_chart.x_labels = map(str, range(1, 12))
    line_chart.add('Network Usage %', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('GPU Usage %',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    line_chart.add('Disk usage %',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('CPU Usage %',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])

    return line_chart.render(is_unicode=True)