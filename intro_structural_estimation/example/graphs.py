import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as plt


def graphs_smoothing_functions(grid, classical, smooth_1, smooth_2):

    ax = plt.figure(figsize=(12, 8)).add_subplot(111)

    ax.plot(grid, classical, label='Classical', linewidth=5, color='red')
    ax.plot(grid, smooth_1, label='Simulated', linewidth=5, color='blue')
    ax.plot(grid, smooth_2, label='Smoothed', linewidth=5, color='green')

    ax.tick_params(labelsize=18, direction='out', axis='both', top='off', right='off')

    ax.set_yticklabels([])
    ax.set_xlim(-0.5, 0.5)

    ax.set_xlabel(r'$\theta$', fontsize=20)
    ax.set_ylabel('Criterion Function', fontsize=16)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10), fancybox=False,
         frameon=False, shadow=False, ncol=3, fontsize=20)
    plt.savefig('../images/smoothing_functions.png', bbox_inches='tight', format='png')


def graphs_method_moments(x_values, mm_values, msm_values, num_sim):

    ax = plt.figure(figsize=(12, 8)).add_subplot(111)

    ax.plot(x_values, mm_values, label='MM', linewidth=5, color='red')
    ax.plot(x_values, msm_values, label='MSM', linewidth=5, color='blue')

    ax.tick_params(labelsize=18, direction='out', axis='both', top='off', right='off')

    ax.yaxis.get_major_ticks()[0].set_visible(False)
    ax.set_xlim(-0.5, 0.5)
    ax.set_yticklabels([])

    ax.text(-0.26, 0.035, r'$\hat{\theta}_{MM} = 0.00$', fontsize=20)
    ax.text(-0.06, 0.035, r'$\hat{\theta}_{MSM} = 0.10$', fontsize=20)
    ax.text(+0.12, 0.035, r'$\theta_0 = 0.00$', fontsize=20)

    fname = 'criterion_method_moments_' + str(num_sim) + '.png'

    ax.set_xlabel(r'$\theta$', fontsize=20)
    ax.set_ylabel('Criterion Function', fontsize=16)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10), fancybox=False, frameon=False,
        shadow=False, ncol=2, fontsize=20)
    plt.savefig('../images/' + fname, bbox_inches='tight', format='png')


def graphs_maximum_likelihood(grid, classical_values, simulated_values, num_sim):

    ax = plt.figure(figsize=(12, 8)).add_subplot(111)

    ax.plot(grid, classical_values, label='ML', linewidth=5, color='red')
    ax.plot(grid, simulated_values, label='SML', linewidth=5, color='blue')

    ax.tick_params(labelsize=18, direction='out', axis='both', top='off', right='off')

    ax.yaxis.get_major_ticks()[0].set_visible(False)
    ax.set_xlim(-0.5, 0.5)
    ax.set_yticklabels([])

    ax.text(-0.26, -77000, r'$\hat{\theta}_{ML} = 0.00$', fontsize=20)

    if num_sim == 100:
        ax.text(-0.06, -77000, r'$\hat{\theta}_{SML} = 0.01$', fontsize=20)
    else:
        ax.text(-0.06, -77000, r'$\hat{\theta}_{SML} = 0.00$', fontsize=20)

    ax.text(+0.12, -77000, r'$\theta_0 = 0.00$', fontsize=20)

    fname = 'criterion_maximum_likelihood_' + str(num_sim) +'.png'

    ax.set_xlabel(r'$\theta$', fontsize=20)
    ax.set_ylabel('Criterion Function', fontsize=16)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10), fancybox=False, frameon=False,
        shadow=False, ncol=2, fontsize=20)

    plt.savefig('../images/' + fname, bbox_inches='tight', format='png')

