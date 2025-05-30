%%%%% Gaussian Filter me thn arxikh (A, Initial)
%%% small window (=4)
x = 1:100;
A = cos(2*pi*0.05*x + 2*pi*rand) + 0.5*randn(1,100);
[B, window] = smoothdata(A,'gaussian');
window

%%%%% Smooth the original data with a larger window of length 20.
C = smoothdata(A, 'gaussian', 20);

%%%%% Plot the smoothed data for both window lengths
plot(x, A, '--', x, B, '-o', x, C, '-x')
legend('A - Initial with noise', 'B - Small Window = 4', 'C - Large Window = 20')
title('Gaussian Filter Smoothing in MATLAB')
xlabel('Sample')
ylabel('Amplitude')
