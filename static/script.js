const BASE_URL = 'https://book-explorer-api.onrender.com'; // Replace with your Render or localhost URL

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
      alert("Book added!");
      fetchBooks();
    } else {
      alert("Failed to add book");
    }
  });

  document.getElementById("search").addEventListener("input", (e) => {
    fetchBooks(e.target.value);
  });
});

async function fetchBooks(query = "") {
  try {
    const res = await fetch(`${BASE_URL}/books?q=${query}`);
    const books = await res.json();
    const list = document.getElementById("bookList");
    list.innerHTML = "";
    books.forEach(book => {
      const li = document.createElement("li");
      li.innerHTML = `<strong>${book.title}</strong> by ${book.author} (${book.year})<br>
                      <em>${book.genre}</em><br>
                      ${book.description}<br>
                      <button onclick="deleteBook(${book.id})">Delete</button>`;
      list.appendChild(li);
    });
  } catch (err) {
    document.getElementById("bookList").innerText = "Failed to load books.";
  }
}

async function deleteBook(id) {
  const res = await fetch(`${BASE_URL}/books/${id}`, {
    method: "DELETE",
  });
  if (res.ok) {
    alert("Book deleted!");
    fetchBooks();
  } else {
    alert("Failed to delete book.");
  }
}
