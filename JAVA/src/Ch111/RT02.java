package Ch111;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class RT02 {
    
    private static String id = "root";   // DB 사용자 이름
    private static String pw = "1234";   // DB 비밀번호
    private static String url = "jdbc:mysql://localhost:3306/tmpdb"; // DB 주소

    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(url, id, pw);
    }

    public static List<BookDto> executeQuery(String sql, Object... params) throws SQLException {
        List<BookDto> bookList = new ArrayList<>();
        try (Connection conn = getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            
            for (int i = 0; i < params.length; i++) {
                pstmt.setObject(i + 1, params[i]);
            }
            
            try (ResultSet rs = pstmt.executeQuery()) {
                while (rs.next()) {
                    bookList.add(new BookDto(
                            rs.getLong("bookCode"),
                            rs.getString("bookName"),
                            rs.getString("publisher"),
                            rs.getString("isbn")
                    ));
                }
            }
        }
        return bookList;
    }

    public static List<BookDto> selectAll() throws SQLException {
        String sql = "SELECT * FROM books";
        return executeQuery(sql);
    }

    public static BookDto select(Long bookCode) throws SQLException {
        String sql = "SELECT * FROM books WHERE bookCode = ?";
        List<BookDto> result = executeQuery(sql, bookCode);
        return result.isEmpty() ? null : result.get(0);
    }

    public static int executeUpdate(String sql, Object... params) throws SQLException {
        try (Connection conn = getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
             
            for (int i = 0; i < params.length; i++) {
                pstmt.setObject(i + 1, params[i]);
            }
            return pstmt.executeUpdate();
        }
    }

    public static int insertBook(BookDto bookDto) throws SQLException {
        String sql = "INSERT INTO books (bookCode, bookName, publisher, isbn) VALUES (?, ?, ?, ?)";
        return executeUpdate(sql, bookDto.getBookCode(), bookDto.getBookName(), bookDto.getPublisher(), bookDto.getIsbn());
    }

    public static int updateBook(BookDto bookDto) throws SQLException {
        String sql = "UPDATE books SET bookName = ?, publisher = ?, isbn = ? WHERE bookCode = ?";
        return executeUpdate(sql, bookDto.getBookName(), bookDto.getPublisher(), bookDto.getIsbn(), bookDto.getBookCode());
    }

    public static int deleteBook(Long bookCode) throws SQLException {
        String sql = "DELETE FROM books WHERE bookCode = ?";
        return executeUpdate(sql, bookCode);
    }

    public static void main(String[] args) {
        try {
            insertBook(new BookDto(1L, "도서명1", "출판사명1", "isbn-1"));
            insertBook(new BookDto(2L, "도서명2", "출판사명2", "isbn-2"));
            insertBook(new BookDto(3L, "도서명3", "출판사명3", "isbn-3"));

            List<BookDto> allBooks = selectAll();
            System.out.println("전체 도서 목록:");
            allBooks.forEach(System.out::println);

            BookDto book = select(1L);
            System.out.println("1번 책 조회: " + book);

            book.setBookName("수정된 도서명");
            book.setPublisher("수정된 출판사");
            updateBook(book);

            deleteBook(2L);

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}

