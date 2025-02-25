body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    text-align: center;
    background-color: #f4f4f4;
    transition: background 0.3s, color 0.3s;
}

header {
    background: #333;
    color: white;
    padding: 15px 0;
}

nav ul {
    list-style: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: white;
    text-decoration: none;
}

section {
    margin: 50px;
    padding: 20px;
    background: white;
    border-radius: 5px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

button {
    padding: 10px 20px;
    border: none;
    background: #007bff;
    color: white;
    font-size: 16px;
    cursor: pointer;
}

button:hover {
    background: #0056b3;
}

/* Chế độ tối */
.dark-mode {
    background-color: #222;
    color: white;
}

.dark-mode section {
    background: #333;
}