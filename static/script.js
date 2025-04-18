const BASE_URL = 'https://book-explorer-api.onrender.com';

document.addEventListener("DOMContentLoaded", () => {
  fetchBooks();

  document.getElementById("addBookForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const bookData = {
      title: document.getElementById("title").value,
      author: document.getElementById("author").value,
      year: parseInt(document.getElementById("year").value),
      description: document.getElementById("description").value,
      genre: document.getElementById("genre").value,
    };

    const res = await fetch(`${BASE_URL}/books`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(bookData),
    });

    if (res.ok) {
      alert("✅ Book added!");
      document.getElementById("addBookForm").reset();
      fetchBooks();
    } else {
      alert("❌ Failed to add book. Try again.");
    }
  });

  document.getElementById("search").addEventListener("input", (e) => {
    fetchBooks(e.target.value);
  });
});

async function fetchBooks(query = "") {
  const list = document.getElementById("bookList");
  list.innerHTML = "<li>⏳ Loading books...</li>";

  try {
    const res = await fetch(`${BASE_URL}/books`);
    const books = await res.json();

    const filteredBooks = books.filter(book =>
      book.title.toLowerCase().includes(query.toLowerCase()) ||
      book.author.toLowerCase().includes(query.toLowerCase())
    );

    list.innerHTML = "";

    if (filteredBooks.length === 0) {
      list.innerHTML = "<li>No books found.</li>";
      return;
    }

    filteredBooks.forEach(book => {
      const li = document.createElement("li");
      li.classList.add("book-card"); // style like other cards

      li.innerHTML = `
        <h3>${book.title}</h3>
        <p><strong>Author:</strong> ${book.author}</p>
        <p><strong>Year:</strong> ${book.year}</p>
        <p><strong>Genre:</strong> ${book.genre}</p>
        <p>${book.description}</p>
        <button class="delete-btn" onclick="deleteBook(${book.id})">Delete</button>
      `;
      list.appendChild(li);
    });
  } catch (err) {
    list.innerHTML = "<li>❌ Failed to load books. Please try again later.</li>";
    console.error(err);
  }
}

async function deleteBook(id) {
  const confirmDelete = confirm("Are you sure you want to delete this book?");
  if (!confirmDelete) return;

  const res = await fetch(`${BASE_URL}/books/${id}`, {
    method: "DELETE",
  });

  if (res.ok) {
    alert("🗑️ Book deleted!");
    fetchBooks();
  } else {
    alert("❌ Failed to delete book.");
  }
}
