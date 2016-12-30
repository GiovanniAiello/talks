import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as plt


def graphs_smoothing_functions(grid, values_0_10, values_0_25, values_0_75):
    pass
    ax = plt.figure(figsize=(12, 8)).add_subplot(111)

    ax.plot(grid, values_0_10, label='0.10', linewidth=5, color='red')
    ax.plot(grid, values_0_25, label='0.25', linewidth=5, color='blue')
    ax.plot(grid, values_0_75, label='0.75', linewidth=5, color='green')

    #
    ax.tick_params(labelsize=18, direction='out', axis='both', top='off',
        right='off')
    #
    # # Remove first element on y-axis
    ax.yaxis.get_major_ticks()[0].set_visible(False)
    ax.set_xlim(-3, 3)
    ax.set_ylim(0.0, 1.0)
    #
    #
    # # # labels
    # ax.set_xlabel(r'$\theta$', fontsize=20)
    # ax.set_ylabel('Criterion Function', fontsize=16)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10), fancybox=False,
         frameon=False, shadow=False, ncol=3, fontsize=20)
    plt.savefig('../images/smoothing_functions.png', bbox_inches='tight', format='png')
    #


def graphs_method_moments(x_values, mm_values, msm_values, num_sim):

    ax = plt.figure(figsize=(12, 8)).add_subplot(111)

    ax.plot(x_values, mm_values, label='MM', linewidth=5, color='red')
    ax.plot(x_values, msm_values, label='MSM', linewidth=5, color='blue')

    ax.tick_params(labelsize=18, direction='out', axis='both', top='off',
        right='off')

    # Remove first element on y-axis
    ax.yaxis.get_major_ticks()[0].set_visible(False)
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)
    ax.set_yticklabels([])

    ax.text(0.225, 0.90, r'$\hat{\theta}_{MM} = 0.49$', fontsize=20)
    ax.text(0.425, 0.90, r'$\hat{\theta}_{MSM} = 0.55$', fontsize=20)
    ax.text(0.625, 0.90, r'$\theta_0 = 0.50$', fontsize=20)
    fname = 'criterion_method_moments_' + str(num_sim) +'.png'

    # # labels
    ax.set_xlabel(r'$\theta$', fontsize=20)
    ax.set_ylabel('Criterion Function', fontsize=16)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10), fancybox=False,
        frameon=False, shadow=False, ncol=2, fontsize=20)
    plt.savefig('../images/' + fname, bbox_inches='tight',
        format='png')


def graphs_maximum_likelihood(x_values, ml_values, sml_values, num_sim):

    ax = plt.figure(figsize=(12, 8)).add_subplot(111)

    ax.plot(x_values, ml_values, label='ML', linewidth=5, color='red')
    ax.plot(x_values, sml_values, label='SML', linewidth=5, color='blue')

    ax.tick_params(labelsize=18, direction='out', axis='both', top='off',
        right='off')
    # Remove first element on y-axis
    ax.yaxis.get_major_ticks()[0].set_visible(False)
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)
    ax.set_yticklabels([])

    ax.text(0.225, 0.90, r'$\hat{\theta}_{ML} = 0.49$', fontsize=20)
    ax.text(0.425, 0.90, r'$\hat{\theta}_{SML} = 0.55$', fontsize=20)
    ax.text(0.625, 0.90, r'$\theta_0 = 0.50$', fontsize=20)

    fname = 'criterion_maximum_likelihood_' + str(num_sim) +'.png'
    # # labels
    ax.set_xlabel(r'$\theta$', fontsize=20)
    ax.set_ylabel('Criterion Function', fontsize=16)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10), fancybox=False,
        frameon=False, shadow=False, ncol=2, fontsize=20)
    plt.savefig('../images/' + fname, bbox_inches='tight', format='png')

