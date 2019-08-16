import matplotlib.pyplot as plt
import pygal



def plot_points(team_names, values, color, year_str, league, save = True, show = False, folder_png = "plots_png"):
    plt.figure(figsize = (25,14))
    plt.barh(y = team_names, width = values, color = color)
    plt.title('{} - Points per team ({})'.format(league, year_str), fontsize = 40)
    plt.ylabel('Club', fontsize = 30)
    plt.xlabel('Points', fontsize = 30)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 15)
    plt.xlim(0, max(values)+7)
    plt.text(3* values[-1] / 4, 8, 'Created by Nishant Rao\nTwitter: @nishant173',
             fontsize = 30, color = 'black',
             horizontalalignment = 'center',
             verticalalignment = 'center',
             alpha = 0.6)
    plt.grid()
    for i, v in enumerate(values):
        plt.text(v + 0.6, i + .1, str(v), fontweight = 'bold', fontsize = 24, color = color)
    if(save == True):
        plt.savefig("{}/1 - {} - Points per team ({}).png".format(folder_png, league, year_str))
    if(show == True):
        plt.show()


def plot_gd(team_names, values, color, year_str, league, save = True, show = False, folder_png = "plots_png"):
    plt.figure(figsize = (25,14))
    plt.barh(y = team_names, width = values, color = color)
    plt.title('{} - Goal Difference per team ({})'.format(league, year_str), fontsize = 40)
    plt.ylabel('Club', fontsize = 30)
    plt.xlabel('GD', fontsize = 30)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 15)
    plt.xlim(min(values) - 7, max(values) + 7)
    plt.text(3* values[-1] / 4, 8, 'Created by Nishant Rao\nTwitter: @nishant173',
             fontsize = 30, color = 'black',
             horizontalalignment = 'center',
             verticalalignment = 'center',
             alpha = 0.6)
    plt.grid()
    for i, v in enumerate(values):
        plt.text(v + 0.6, i + .1, str(v), fontweight = 'bold', fontsize = 24, color = "black")
    if(save == True):
        plt.savefig("{}/2 - {} - Goal Difference per team ({}).png".format(folder_png, league, year_str))
    if(show == True):
        plt.show()


def plot_wins(team_names, values, color, year_str, league, save = True, show = False, folder_png = "plots_png"):
    plt.figure(figsize = (25,14))
    plt.barh(y = team_names, width = values, color = color)
    plt.title('{} - Games Won per team ({})'.format(league, year_str), fontsize = 40)
    plt.ylabel('Club', fontsize = 30)
    plt.xlabel('Wins', fontsize = 30)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 15)
    plt.xlim(0, max(values) + 2)
    plt.text(3 * values[-1] / 4, 8, 'Created by Nishant Rao\nTwitter: @nishant173',
             fontsize = 30, color = 'black',
             horizontalalignment = 'center',
             verticalalignment = 'center',
             alpha = 0.6)
    plt.grid()
    for i, v in enumerate(values):
        plt.text(v + 0.6, i + .1, str(v), fontweight = 'bold', fontsize = 24, color = color)
    if(save == True):
        plt.savefig("{}/5 - {} - Games Won per team ({}).png".format(folder_png, league, year_str))
    if(show == True):
        plt.show()


def plot_losses(team_names, values, color, year_str, league, save = True, show = False, folder_png = "plots_png"):
    plt.figure(figsize = (25,14))
    plt.barh(y = team_names, width = values, color = color)
    plt.title('{} - Games Lost per team ({})'.format(league, year_str), fontsize = 40)
    plt.ylabel('Club', fontsize = 30)
    plt.xlabel('Losses', fontsize = 30)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 15)
    plt.xlim(0, max(values) + 2)
    plt.text(values[0] / 2, 8, 'Created by Nishant Rao\nTwitter: @nishant173',
             fontsize = 30, color = 'black',
             horizontalalignment = 'center',
             verticalalignment = 'center',
             alpha = 0.6)
    plt.grid()
    for i, v in enumerate(values):
        plt.text(v + 0.6, i + .1, str(v), fontweight = 'bold', fontsize = 24, color = color)
    if(save == True):
        plt.savefig("{}/6 - {} - Games Lost per team ({}).png".format(folder_png, league, year_str))
    if(show == True):
        plt.show()


def plot_draws(team_names, values, color, year_str, league, save = True, show = False, folder_png = "plots_png"):
    plt.figure(figsize = (25,14))
    plt.barh(y = team_names, width = values, color = color)
    plt.title('{} - Games Drawn per team ({})'.format(league, year_str), fontsize = 40)
    plt.ylabel('Club', fontsize = 30)
    plt.xlabel('Draws', fontsize = 30)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 15)
    plt.xlim(0, max(values) + 2)
    plt.text(3 * values[-1] / 4, 8, 'Created by Nishant Rao\nTwitter: @nishant173',
             fontsize = 30, color = 'black',
             horizontalalignment = 'center',
             verticalalignment = 'center',
             alpha = 0.6)
    plt.grid()
    for i, v in enumerate(values):
        plt.text(v + 0.6, i + .1, str(v), fontweight = 'bold', fontsize = 24, color = color)
    if(save == True):
        plt.savefig("{}/7 - {} - Games Drawn per team ({}).png".format(folder_png, league, year_str))
    if(show == True):
        plt.show()


def plot_gf(team_names, values, color, year_str, league, save = True, show = False, folder_png = "plots_png"):
    plt.figure(figsize = (25,14))
    plt.barh(y = team_names, width = values, color = color)
    plt.title('{} - Goals For per team ({})'.format(league, year_str), fontsize = 40)
    plt.ylabel('Club', fontsize = 30)
    plt.xlabel('GF', fontsize = 30)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 15)
    plt.xlim(0, max(values) + 2)
    plt.text(3 * values[-1] / 4, 8, 'Created by Nishant Rao\nTwitter: @nishant173',
             fontsize = 30, color = 'black',
             horizontalalignment = 'center',
             verticalalignment = 'center',
             alpha = 0.6)
    plt.grid()
    for i, v in enumerate(values):
        plt.text(v + 0.6, i + .1, str(v), fontweight = 'bold', fontsize = 24, color = "#0D793A")
    if(save == True):
        plt.savefig("{}/3 - {} - Goals For per team ({}).png".format(folder_png, league, year_str))
    if(show == True):
        plt.show()


def plot_ga(team_names, values, color, year_str, league, save = True, show = False, folder_png = "plots_png"):
    plt.figure(figsize = (25,14))
    plt.barh(y = team_names, width = values, color = color)
    plt.title('{} - Goals Allowed per team ({})'.format(league, year_str), fontsize = 40)
    plt.ylabel('Club', fontsize = 30)
    plt.xlabel('GA', fontsize = 30)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 15)
    plt.xlim(0, max(values) + 2)
    plt.text(3 * values[-1] / 4, 8, 'Created by Nishant Rao\nTwitter: @nishant173',
             fontsize = 30, color = 'black',
             horizontalalignment = 'center',
             verticalalignment = 'center',
             alpha = 0.6)
    plt.grid()
    for i, v in enumerate(values):
        plt.text(v + 0.6, i + .1, str(v), fontweight = 'bold', fontsize = 24, color = color)
    if(save == True):
        plt.savefig("{}/4 - {} - Goals Allowed per team ({}).png".format(folder_png, league, year_str))
    if(show == True):
        plt.show()


def plot_gp(team_names, values, color, year_str, league, save = True, show = False, folder_png = "plots_png"):
    plt.figure(figsize = (25,14))
    plt.barh(y = team_names, width = values, color = color)
    plt.title('{} - Games Played per team ({})'.format(league, year_str), fontsize = 40)
    plt.ylabel('Club', fontsize = 30)
    plt.xlabel('Games Played', fontsize = 30)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 15)
    plt.xlim(0, max(values) + 2)
    plt.text(3 * values[-1] / 4, 8, 'Created by Nishant Rao\nTwitter: @nishant173',
             fontsize = 30, color = 'black',
             horizontalalignment = 'center',
             verticalalignment = 'center',
             alpha = 0.6)
    plt.grid()
    for i, v in enumerate(values):
        plt.text(v + 0.6, i + .1, str(v), fontweight = 'bold', fontsize = 24, color = color)
    if(save == True):
        plt.savefig("{}/8 - {} - Games Played per team ({}).png".format(folder_png, league, year_str))
    if(show == True):
        plt.show()



def plot_pygal_all(year_str, folder_svg, number_of_teams, clubs_pygal, points_pygal, gd_pygal, gf_pygal, ga_pygal, wins_pygal, losses_pygal, draws_pygal, gp_pygal, league):
    bar_chart_h = pygal.HorizontalBar(title = u'{} - Points per team ({})'.format(league, year_str), x_title = 'Points', y_title = 'Club')
    for i in range(0, number_of_teams):
        bar_chart_h.add(clubs_pygal[i], points_pygal[i])
    bar_chart_h.render_to_file('{}/1 - {} - Points per team ({}).svg'.format(folder_svg, league, year_str))
    
    
    bar_chart_h = pygal.HorizontalBar(title = u'{} - Goal Difference per team ({})'.format(league, year_str), x_title = 'GD', y_title = 'Club')
    for i in range(0, number_of_teams):
        bar_chart_h.add(clubs_pygal[i], gd_pygal[i])
    bar_chart_h.render_to_file('{}/2 - {} - Goal Difference per team ({}).svg'.format(folder_svg, league, year_str))
    
    
    bar_chart = pygal.HorizontalBar(title = u'{} - Goals For per team ({})'.format(league, year_str), x_title = 'GF', y_title = 'Club')
    for i in range(0, number_of_teams):
        bar_chart.add(clubs_pygal[i], gf_pygal[i])
    bar_chart.render_to_file('{}/3 - {} - Goals For per team ({}).svg'.format(folder_svg, league, year_str))
    
    
    bar_chart = pygal.HorizontalBar(title = u'{} - Goals Allowed per team ({})'.format(league, year_str), x_title = 'GA', y_title = 'Club')
    for i in range(0, number_of_teams):
        bar_chart.add(clubs_pygal[i], ga_pygal[i])
    bar_chart.render_to_file('{}/4 - {} - Goals Allowed per team ({}).svg'.format(folder_svg, league, year_str))
    
    
    bar_chart = pygal.HorizontalBar(title = u'{} - Wins per team ({})'.format(league, year_str), x_title = 'Wins', y_title = 'Club')
    for i in range(0, number_of_teams):
        bar_chart.add(clubs_pygal[i], wins_pygal[i])
    bar_chart.render_to_file('{}/5 - {} - Wins per team ({}).svg'.format(folder_svg, league, year_str))
    
    
    bar_chart = pygal.HorizontalBar(title = u'{} - Losses per team ({})'.format(league, year_str), x_title = 'Losses', y_title = 'Club')
    for i in range(0, number_of_teams):
        bar_chart.add(clubs_pygal[i], losses_pygal[i])
    bar_chart.render_to_file('{}/6 - {} - Losses per team ({}).svg'.format(folder_svg, league, year_str))
    
    
    bar_chart = pygal.HorizontalBar(title = u'{} - Draws per team ({})'.format(league, year_str), x_title = 'Draws', y_title = 'Club')
    for i in range(0, number_of_teams):
        bar_chart.add(clubs_pygal[i], draws_pygal[i])
    bar_chart.render_to_file('{}/7 - {} - Draws per team ({}).svg'.format(folder_svg, league, year_str))
    
    
    bar_chart = pygal.HorizontalBar(title = u'{} - Games Played per team ({})'.format(league, year_str), x_title = 'Games Played', y_title = 'Club')
    for i in range(0, number_of_teams):
        bar_chart.add(clubs_pygal[i], gp_pygal[i])
    bar_chart.render_to_file('{}/8 - {} - Games Played per team ({}).svg'.format(folder_svg, league, year_str))



def plot_sorted_all(df_sorted_by, year_str, sorted_plots_folder_name, league):
    plt.figure(figsize = (25,14))
    df_sorted_by.sort_values(by = 'WonW')['WonW'].plot(kind = 'barh')
    plt.title('{} - Games Won per team ({})'.format(league, year_str), fontsize = 40)
    plt.ylabel('Club', fontsize = 30)
    plt.xlabel('Wins', fontsize = 30)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 15)
    values = df_sorted_by.sort_values(by = 'WonW')['WonW']
    plt.text(3 * values.iloc[-1] / 4, 8,
             'Created by Nishant Rao\nTwitter: @nishant173',
             fontsize = 30, color = 'black',
             horizontalalignment = 'center',
             verticalalignment = 'center',
             alpha = 0.6)
    
    for i, v in enumerate(values):
        plt.text(v + 0.6, i + .1, str(v), fontweight = 'bold', fontsize = 24)
    plt.savefig("{}/{} - Games Won per team ({}).png".format(sorted_plots_folder_name, league, year_str))


    plt.figure(figsize = (25,14))
    df_sorted_by.sort_values(by = 'LostL')['LostL'].plot(kind = 'barh')
    plt.title('{} - Games Lost per team ({})'.format(league, year_str), fontsize = 40)
    plt.ylabel('Club', fontsize = 30)
    plt.xlabel('Losses', fontsize = 30)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 15)
    values = df_sorted_by.sort_values(by = 'LostL')['LostL']
    plt.text(3 * values.iloc[-1] / 4, 8,
             'Created by Nishant Rao\nTwitter: @nishant173',
             fontsize = 30, color = 'black',
             horizontalalignment = 'center',
             verticalalignment = 'center',
             alpha = 0.6)
    
    for i, v in enumerate(values):
        plt.text(v + 0.6, i + .1, str(v), fontweight = 'bold', fontsize = 24)
    plt.savefig("{}/{} - Games Lost per team ({}).png".format(sorted_plots_folder_name, league, year_str))


    plt.figure(figsize = (25,14))
    df_sorted_by.sort_values(by = 'DrawnD')['DrawnD'].plot(kind = 'barh')
    plt.title('{} - Games Drawn per team ({})'.format(league, year_str), fontsize = 40)
    plt.ylabel('Club', fontsize = 30)
    plt.xlabel('Draws', fontsize = 30)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 15)
    values = df_sorted_by.sort_values(by = 'DrawnD')['DrawnD']
    plt.text(3 * values.iloc[-1] / 4, 8,
             'Created by Nishant Rao\nTwitter: @nishant173',
             fontsize = 30, color = 'black',
             horizontalalignment = 'center',
             verticalalignment = 'center',
             alpha = 0.6)
    
    for i, v in enumerate(values):
        plt.text(v + 0.6, i + .1, str(v), fontweight = 'bold', fontsize = 24)
    plt.savefig("{}/{} - Games Drawn per team ({}).png".format(sorted_plots_folder_name, league, year_str))


    plt.figure(figsize = (25,14))
    df_sorted_by.sort_values(by = 'GF')['GF'].plot(kind = 'barh')
    plt.title('{} - Goals For per team ({})'.format(league, year_str), fontsize = 40)
    plt.ylabel('Club', fontsize = 30)
    plt.xlabel('Goals For', fontsize = 30)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 15)
    values = df_sorted_by.sort_values(by = 'GF')['GF']
    plt.text(3 * values.iloc[-1] / 4, 8,
             'Created by Nishant Rao\nTwitter: @nishant173',
             fontsize = 30, color = 'black',
             horizontalalignment = 'center',
             verticalalignment = 'center',
             alpha = 0.6)
    
    for i, v in enumerate(values):
        plt.text(v + 0.6, i + .1, str(v), fontweight = 'bold', fontsize = 24)
    plt.savefig("{}/{} - Goals For per team ({}).png".format(sorted_plots_folder_name, league, year_str))
    
    
    plt.figure(figsize = (25,14))
    df_sorted_by.sort_values(by = 'GA')['GA'].plot(kind = 'barh')
    plt.title('{} - Goals Allowed per team ({})'.format(league, year_str), fontsize = 40)
    plt.ylabel('Club', fontsize = 30)
    plt.xlabel('Goals Allowed', fontsize = 30)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 15)
    values = df_sorted_by.sort_values(by = 'GA')['GA']
    plt.text(3 * values.iloc[-1] / 4, 8,
             'Created by Nishant Rao\nTwitter: @nishant173',
             fontsize = 30, color = 'black',
             horizontalalignment = 'center',
             verticalalignment = 'center',
             alpha = 0.6)
    
    for i, v in enumerate(values):
        plt.text(v + 0.6, i + .1, str(v), fontweight = 'bold', fontsize = 24)
    plt.savefig("{}/{} - Goals Allowed per team ({}).png".format(sorted_plots_folder_name, league, year_str))
    
    
    plt.figure(figsize = (25,14))
    df_sorted_by.sort_values(by = 'GD')['GD'].plot(kind = 'barh')
    plt.title('{} - Goal Difference per team ({})'.format(league, year_str), fontsize = 40)
    plt.ylabel('Club', fontsize = 30)
    plt.xlabel('Goal Difference', fontsize = 30)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 15)
    values = df_sorted_by.sort_values(by = 'GD')['GD']
    plt.text(3 * values.iloc[-1] / 4, 8,
             'Created by Nishant Rao\nTwitter: @nishant173',
             fontsize = 30, color = 'black',
             horizontalalignment = 'center',
             verticalalignment = 'center',
             alpha = 0.6)
    
    for i, v in enumerate(values):
        plt.text(v + 0.6, i + .1, str(v), fontweight = 'bold', fontsize = 24)
    plt.savefig("{}/{} - Goal Difference per team ({}).png".format(sorted_plots_folder_name, league, year_str))
    
    
    plt.figure(figsize = (25,14))
    df_sorted_by.sort_values(by = 'PointsPts')['PointsPts'].plot(kind = 'barh')
    plt.title('{} - Points per team ({})'.format(league, year_str), fontsize = 40)
    plt.ylabel('Club', fontsize = 30)
    plt.xlabel('Points', fontsize = 30)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 15)
    values = df_sorted_by.sort_values(by = 'PointsPts')['PointsPts']
    plt.text(3 * values.iloc[-1] / 4, 8,
             'Created by Nishant Rao\nTwitter: @nishant173',
             fontsize = 30, color = 'black',
             horizontalalignment = 'center',
             verticalalignment = 'center',
             alpha = 0.6)
    
    for i, v in enumerate(values):
        plt.text(v + 0.6, i + .1, str(v), fontweight = 'bold', fontsize = 24)
    plt.savefig("{}/{} - Points per team ({}).png".format(sorted_plots_folder_name, league, year_str))
