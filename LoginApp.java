Sure, here's an example of a basic Java login application using the Swing library. This example includes a simple username and password validation.

```java
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class LoginApp extends JFrame {
    private JTextField usernameField;
    private JPasswordField passwordField;
    private JButton loginButton;
    private JLabel errorLabel;

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new LoginApp();
            }
        });
    }

    public LoginApp() {
        setTitle("Login App");
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(null);

        JLabel usernameLabel = new JLabel("Username:");
        usernameLabel.setBounds(10, 10, 80, 25);
        add(usernameLabel);

        usernameField = new JTextField();
        usernameField.setBounds(100, 10, 180, 25);
        add(usernameField);

        JLabel passwordLabel = new JLabel("Password:");
        passwordLabel.setBounds(10, 40, 80, 25);
        add(passwordLabel);

        passwordField = new JPasswordField();
        passwordField.setBounds(100, 40, 180, 25);
        add(passwordField);

        loginButton = new JButton("Login");
        loginButton.setBounds(100, 70, 100, 30);
        loginButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String username = usernameField.getText();
                String password = new String(passwordField.getPassword());

                if ("admin".equals(username) && "password".equals(password)) {
                    JOptionPane.showMessageDialog(LoginApp.this, "Login successful!");
                } else {
                    errorLabel.setText("Invalid username or password");
                }
            }
        });
        add(loginButton);

        errorLabel = new JLabel();
        errorLabel.setBounds(10, 110, 280, 25);
        add(errorLabel);

        setVisible(true);
    }
}
```

This code creates a simple login form with username and password fields. When the user clicks "Login", it checks if the username is "admin" and the password is "password". If they match, it shows a success message; otherwise, it displays an error message.

Note: This is just a basic example for demonstration purposes. In a real-world application, you would not store passwords in plain text like this. Instead, you should hash and salt the passwords before storing them in a database and compare the hashes when verifying user credentials.