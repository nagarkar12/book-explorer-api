const bookList = document.getElementById('book-list');

fetch('https://book-explorer-api.onrender.com/books')
  .then(res => res.json())
  .then(data => {
    data.forEach(book => {
      const div = document.createElement('div');
      div.classList.add('book');
      div.innerHTML = `
        <h3>${book.title}</h3>
        <p><strong>Author:</strong> ${book.author}</p>
        <p><strong>ID:</strong> ${book.id}</p>
      `;
      bookList.appendChild(div);
    });
  })
  .catch(error => {
    bookList.innerHTML = `<p>Error fetching books </p>`;
    console.error(error);
  });
