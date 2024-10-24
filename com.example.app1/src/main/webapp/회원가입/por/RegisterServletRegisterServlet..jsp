<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<% 
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

@WebServlet("/register")
public class RegisterServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Retrieve form data
        String userid = request.getParameter("userid");
        String password = request.getParameter("password");
        String email = request.getParameter("useremail");

        // Address and phone number fields
        String address = request.getParameter("address");
        String additionalAddress = request.getParameter("additionalAddress");
        String phoneNumber = request.getParameter("phonenumber");

        // Server-side validation
        if (!phoneNumber.matches("[0-9]{3}-[0-9]{3,4}-[0-9]{4}")) {
            throw new ServletException("Invalid phone number format. Please use the format 010-1234-5678.");
        }
        
        if (address == null || address.trim().isEmpty()) {
            throw new ServletException("Address cannot be empty.");
        }

        // Database connection and saving logic
        Connection connection = null;
        PreparedStatement preparedStatement = null;

        try {
            // 1. Load MySQL JDBC Driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // 2. Establish a connection to the database
            String dbURL = "jdbc:mysql://localhost:3306/your_database_name";
            String dbUser = "your_db_username";
            String dbPassword = "your_db_password";
            connection = DriverManager.getConnection(dbURL, dbUser, dbPassword);

            // 3. Prepare the SQL insert statement
            String sql = "INSERT INTO users (userid, password, email, address, additionalAddress, phoneNumber) VALUES (?, ?, ?, ?, ?, ?)";
            preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setString(1, userid);
            preparedStatement.setString(2, password);
            preparedStatement.setString(3, email);
            preparedStatement.setString(4, address);
            preparedStatement.setString(5, additionalAddress);
            preparedStatement.setString(6, phoneNumber);

            // 4. Execute the insert
            int rowsInserted = preparedStatement.executeUpdate();
            if (rowsInserted > 0) {
                System.out.println("A new user was inserted successfully!");
            }

            // 5. Redirect to success page
            response.sendRedirect("success.html");
        } catch (SQLException | ClassNotFoundException e) {
            throw new ServletException("Database connection error: " + e.getMessage());
        } finally {
            // Close resources
            try {
                if (preparedStatement != null) preparedStatement.close();
                if (connection != null) connection.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}

    %>