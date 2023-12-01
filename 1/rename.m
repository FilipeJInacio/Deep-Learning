% Define XOR-like function for inputs -1 and 1
xor_custom = @(a, b) xor(a == 1, b == 1);

% Create a grid of inputs (-1 and 1)
[x, y] = meshgrid([-1 1], [-1 1]);

% Compute XOR-like function values for all combinations of inputs
z = arrayfun(xor_custom, x, y);

% Plot the XOR-like function
figure;
% Plot Output 0 (blue)
scatter(x(z == 0), y(z == 0), 100, 'b', 'filled');
hold on;

% Plot Output 1 (red)
scatter(x(z == 1), y(z == 1), 100, 'r', 'filled');

% Customize the plot
xlabel('$x_1$', 'Interpreter', 'latex');
ylabel('$x_2$', 'Interpreter', 'latex');
title('$f(x)$', 'Interpreter', 'latex');
axis([-2 2 -2 2]);
grid on;

% Add legends
legend({'-1', '1'}, 'Interpreter', 'latex');
