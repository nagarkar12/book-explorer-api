const apiUrl = 'https://book-explorer-api.onrender.com/books'; // Replace with your actual API URL

document.addEventListener('DOMContentLoaded', () => {
  fetch(apiUrl)
    .then(res => res.json())
    .then(books => {
      const bookList = document.getElementById('book-list');
      bookList.innerHTML = ''; // Clear existing
      books.forEach(book => {
        const div = document.createElement('div');
        div.classList.add('book-card');
        div.innerHTML = `
          <h3>${book.title}</h3>
          <p><strong>Author:</strong> ${book.author}</p>
          <p><strong>Year:</strong> ${book.year}</p>
          <p><strong>Genre:</strong> ${book.genre}</p>
          <p>${book.description}</p>
        `;
        bookList.appendChild(div);
      });
    })
    .catch(err => {
      document.getElementById('book-list').innerHTML = '<p>Failed to load books.</p>';
      console.error(err);
    });
});
