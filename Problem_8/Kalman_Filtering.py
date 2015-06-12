import numpy
import pylab
import random

def frand():
    return 2*(random.random()-0.5)
    
def kalman():
    ''' initial values for the kalman filter '''
    x_est_last = 0
    P_last = 0
    
    ''' the noise in the system '''
    Q = 0.022
    R = 0.617
    
    K = 0
    P = 0
    P_temp = 0;
    x_temp_est = 0;
    x_est = 0;
    
    ''' the 'noisy' value we measured '''
    z_measured = 0.5
    
    ''' the ideal value we wish to measure '''
    z_real = 0.5
    
    ''' initialize with a measurement '''
    x_est_last = z_real + frand() * 0.09
    sum_error_kalman = 0
    sum_error_measure = 0
    
    i = 0
    while i<100:
        ''' do a prediction '''
        x_temp_est = x_est_last
        P_temp = P_last + Q
        
        ''' calculate the kalman gain '''
        K = P_temp * (1.0/(P_temp + R))
        ''' measure '''
        z_measured = z_real + frand()*0.09      # the real measurement + noise
        ''' correct '''
        x_est = x_temp_est + K*(z_measured - x_temp_est)    
        P = (1 - K)*P_temp
        
        pylab.plot(i, z_real, 'bo')      # ideal
        pylab.plot(i, z_measured, 'go')  # measured
        pylab.plot(i, x_est, 'ro')       # kalman

        sum_error_kalman += numpy.fabs(z_real - x_est)
        sum_error_measure += numpy.fabs(z_real - z_measured)
        
        ''' update our last's '''
        P_last = P
        x_est_last = x_est
        i = i + 1
    
    print "Total error if using raw measured : ", sum_error_measure
    print "Total error if using kalman filter : ", sum_error_kalman
    print "Reduction in error : ", 100-((sum_error_kalman/sum_error_measure)*100)
    pylab.title('Kalman Filtering')
    pylab.xlabel('R:kalman / G:measured / B:ideal')
    pylab.show()
    
kalman();
