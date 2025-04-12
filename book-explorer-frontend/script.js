const API_URL = "https://book-explorer-api.onrender.com/books"; // replace with your actual deployed API URL

async function fetchBooks() {
  try {
    const response = await fetch(API_URL);
    const books = await response.json();

    const bookList = document.getElementById("book-list");
    bookList.innerHTML = "";

    books.forEach(book => {
      const bookDiv = document.createElement("div");
      bookDiv.className = "book";
      bookDiv.innerHTML = `
        <h3>${book.title}</h3>
        <p><strong>Author:</strong> ${book.author}</p>
        <p><strong>Rating:</strong> ${book.rating}</p>
      `;
      bookList.appendChild(bookDiv);
    });

  } catch (error) {
    console.error("Failed to fetch books:", error);
  }
}

fetchBooks();
