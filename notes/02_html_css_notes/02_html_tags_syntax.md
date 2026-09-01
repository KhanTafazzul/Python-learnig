# 📑 HTML5 Tags & Complete Syntax Reference Guide

This comprehensive reference covers all core and modern HTML5 tags, their exact syntax, what they do, their key attributes, and practical code examples.

---

## 📑 Quick Navigation
1. [Document Skeleton & Metadata](#1-document-skeleton--metadata)
2. [Semantic Layout & Landmark Tags](#2-semantic-layout--landmark-tags)
3. [Headings & Text Formatting Tags](#3-headings--text-formatting-tags)
4. [Links & Media Elements](#4-links--media-elements)
5. [Lists & Description Containers](#5-lists--description-containers)
6. [Data Tables](#6-data-tables)
7. [Forms & User Inputs](#7-forms--user-inputs)
8. [Interactive & Modern UI Elements](#8-interactive--modern-ui-elements)
9. [Block-Level vs. Inline Elements](#9-block-level-vs-inline-elements)

---

## 1. Document Skeleton & Metadata

These tags define the webpage configuration, character encoding, title, and external resource connections.

### 1.1 `<!DOCTYPE html>`
* **What it does**: Informs the web browser that the document is written in modern **HTML5**. It must always be the very first line of any `.html` file.
* **Syntax**:
  ```html
  <!DOCTYPE html>
  ```

### 1.2 `<html>`
* **What it does**: The root container for the entire webpage. All other HTML tags reside inside it.
* **Key Attributes**: `lang="en"` (specifies the document language for search engines and screen readers).
* **Syntax**:
  ```html
  <html lang="en">
    <!-- All page content goes here -->
  </html>
  ```

### 1.3 `<head>`
* **What it does**: Contains machine-readable **metadata** about the document (title, character set, responsive viewport settings, CSS stylesheets, and favicon links). Content inside `<head>` is **invisible** on the main browser viewport.
* **Syntax**:
  ```html
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio</title>
    <link rel="stylesheet" href="style.css">
  </head>
  ```

### 1.4 `<title>`
* **What it does**: Sets the title displayed on the browser's tab, bookmarks, and search engine search result headlines.
* **Syntax**:
  ```html
  <title>Aman | Full-Stack Developer</title>
  ```

### 1.5 `<meta>`
* **What it does**: Provides document metadata (character encoding, responsive mobile scaling, SEO keywords, author information).
* **Syntax**:
  ```html
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Learn Python and Web Development from scratch.">
  ```

### 1.6 `<link>`
* **What it does**: Connects external stylesheets (CSS), fonts, or favicon icons to the HTML file.
* **Syntax**:
  ```html
  <link rel="stylesheet" href="styles.css">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  ```

### 1.7 `<body>`
* **What it does**: Contains all visible content displayed to the user (text, images, buttons, navigation, headers, footers).
* **Syntax**:
  ```html
  <body>
    <h1>Welcome to My Webpage</h1>
  </body>
  ```

---

## 2. Semantic Layout & Landmark Tags

HTML5 semantic tags clearly describe their meaning to both the browser and the developer, boosting **SEO** and **Web Accessibility**.

```text
+-------------------------------------------------------+
|                       <header>                        |
|   +-----------------------------------------------+   |
|   |                     <nav>                     |   |
|   +-----------------------------------------------+   |
+-------------------------------------------------------+
|                        <main>                         |
|   +-------------------------------+   +-----------+   |
|   |           <section>           |   |  <aside>  |   |
|   |   +-----------------------+   |   | (Sidebar) |   |
|   |   |       <article>       |   |   +-----------+   |
|   |   +-----------------------+   |                   |
|   +-------------------------------+                   |
+-------------------------------------------------------+
|                       <footer>                        |
+-------------------------------------------------------+
```

### 2.1 `<header>`
* **What it does**: Represents introductory content for a page or section (logo, site title, hero intro, navigation wrapper).
* **Syntax**:
  ```html
  <header>
    <h1>Aman's Tech Blog</h1>
    <p>Exploring Python & Web Engineering</p>
  </header>
  ```

### 2.2 `<nav>`
* **What it does**: Defines a block of major navigation links (menus, table of contents).
* **Syntax**:
  ```html
  <nav>
    <a href="#home">Home</a>
    <a href="#projects">Projects</a>
    <a href="#contact">Contact</a>
  </nav>
  ```

### 2.3 `<main>`
* **What it does**: Wraps the central, dominant, and unique content of the `<body>`. There must only be **one** `<main>` element per webpage.
* **Syntax**:
  ```html
  <main>
    <h2>Featured Projects</h2>
    <!-- Main content goes here -->
  </main>
  ```

### 2.4 `<section>`
* **What it does**: Groups related content together under a thematic heading (e.g., "About Section", "Skills Section", "Reviews Section").
* **Syntax**:
  ```html
  <section id="about">
    <h2>About Me</h2>
    <p>I am a developer specializing in Python and frontend interfaces.</p>
  </section>
  ```

### 2.5 `<article>`
* **What it does**: Represents a self-contained, independent piece of content that could be distributed or reused on its own (e.g., a blog post, product card, user comment, news article).
* **Syntax**:
  ```html
  <article>
    <h3>How to Learn Python in 2026</h3>
    <p>Start with fundamentals, build projects daily, and write clean code.</p>
  </article>
  ```

### 2.6 `<aside>`
* **What it does**: Marks content that is indirectly related to the main content (sidebars, author bio cards, related links, advertisements).
* **Syntax**:
  ```html
  <aside>
    <h4>Quick Facts</h4>
    <p>Python was created by Guido van Rossum in 1991.</p>
  </aside>
  ```

### 2.7 `<footer>`
* **What it does**: Appears at the bottom of a page or section, containing copyright notices, privacy policy links, and social media icons.
* **Syntax**:
  ```html
  <footer>
    <p>&copy; 2026 Aman. Built with HTML5 & CSS3.</p>
  </footer>
  ```

### 2.8 `<div>` & `<span>` (Generic Containers)
* **`<div>` (Block container)**: Used to group elements together for CSS styling or JavaScript layout positioning when no semantic tag fits.
* **`<span>` (Inline container)**: Used to wrap a specific word or phrase inside a paragraph for distinct styling (like changing text color).
* **Syntax**:
  ```html
  <div class="card">
    <p>This is a <span class="highlight">crucial</span> point.</p>
  </div>
  ```

---

## 3. Headings & Text Formatting Tags

### 3.1 Headings: `<h1>` to `<h6>`
* **What they do**: Define 6 levels of section headings. `<h1>` is the most important (main page title, use only **once** per page for SEO), down to `<h6>` (least important).
* **Syntax**:
  ```html
  <h1>Main Page Title (Level 1)</h1>
  <h2>Major Section Heading (Level 2)</h2>
  <h3>Sub-heading (Level 3)</h3>
  <h4>Minor Heading (Level 4)</h4>
  <h5>Small Heading (Level 5)</h5>
  <h6>Smallest Heading (Level 6)</h6>
  ```

### 3.2 `<p>` (Paragraph)
* **What it does**: Defines a block of body text. Automatically adds top and bottom spacing in browsers.
* **Syntax**:
  ```html
  <p>HTML is the standard markup language for creating Web pages.</p>
  ```

### 3.3 Text Styling Tags

| Tag | Name | Purpose | Example |
| :--- | :--- | :--- | :--- |
| `<strong>` | Strong Importance | Bold text with semantic importance (SEO + Screen Readers) | `<strong>Critical Warning</strong>` |
| `<b>` | Bold Text | Visually bold without extra semantic weight | `<b>Bold keyword</b>` |
| `<em>` | Emphasis | Italicized text with semantic stress | `<em>Please read carefully</em>` |
| `<i>` | Italic Text | Visually italicized (terms, book titles, icons) | `<i>Homo sapiens</i>` |
| `<mark>` | Highlight | Yellow background highlighted text | `<mark>Search result match</mark>` |
| `<small>` | Small Text | Disclaimers, copyright, and fine print | `<small>Terms and conditions apply.</small>` |
| `<del>` | Deleted Text | Strikethrough text (e.g. old price) | `<del>$50</del>` |
| `<ins>` | Inserted Text | Underlined newly added text (e.g. new price) | `<ins>$35</ins>` |
| `<sup>` | Superscript | Raised text (e.g. math exponents, ordinal dates) | `E = mc<sup>2</sup>` |
| `<sub>` | Subscript | Lowered text (e.g. chemical formulas) | `H<sub>2</sub>O` |
| `<code>` | Inline Code | Monospaced font for code keywords | `Run <code>python app.py</code>` |
| `<pre>` | Preformatted | Preserves exact spaces and line breaks | `<pre>Line 1\n  Line 2</pre>` |
| `<br>` | Line Break | Forces a new line inside a paragraph (self-closing) | `Line 1<br>Line 2` |
| `<hr>` | Horizontal Rule | Horizontal thematic separator line (self-closing) | `<hr>` |

---

## 4. Links & Media Elements

### 4.1 `<a>` (Anchor / Hyperlink)
* **What it does**: Creates clickable hyperlinks to navigate to external websites, other local pages, or jump to section IDs on the same page.
* **Key Attributes**:
  * `href`: The destination URL or file path.
  * `target="_blank"`: Opens the link in a **new browser tab**.
  * `rel="noopener noreferrer"`: Security best practice when opening new tabs.
* **Syntax**:
  ```html
  <!-- External link opening in new tab -->
  <a href="https://google.com" target="_blank" rel="noopener noreferrer">Visit Google</a>

  <!-- Internal page link -->
  <a href="contact.html">Contact Us</a>

  <!-- On-page bookmark jump -->
  <a href="#skills">Jump to Skills Section</a>
  ```

### 4.2 `<img>` (Image)
* **What it does**: Embeds an image on the page (self-closing tag).
* **Key Attributes**:
  * `src`: File path or online image URL.
  * `alt`: **Crucial** text description (read by screen readers and shown if the image fails to load).
  * `width` / `height`: Dimensions in pixels.
* **Syntax**:
  ```html
  <img src="profile.jpg" alt="Aman sitting at his coding workspace" width="300" height="300">
  ```

### 4.3 `<figure>` & `<figcaption>`
* **What it does**: Semantic container for images, diagrams, or charts along with an explanatory caption.
* **Syntax**:
  ```html
  <figure>
    <img src="architecture.png" alt="System architecture flow">
    <figcaption>Figure 1: Flask request-response lifecycle.</figcaption>
  </figure>
  ```

### 4.4 `<audio>` & `<video>`
* **What they do**: Native HTML5 media players without requiring third-party plugins.
* **Syntax**:
  ```html
  <!-- Audio Player -->
  <audio controls>
    <source src="podcast.mp3" type="audio/mpeg">
    Your browser does not support audio.
  </audio>

  <!-- Video Player -->
  <video controls width="640" poster="thumbnail.jpg">
    <source src="tutorial.mp4" type="video/mp4">
    Your browser does not support video.
  </video>
  ```

---

## 5. Lists & Description Containers

### 5.1 `<ul>` (Unordered List)
* **What it does**: Bulleted list of items where order does not matter.
* **Syntax**:
  ```html
  <ul>
    <li>HTML5</li>
    <li>CSS3</li>
    <li>Python</li>
  </ul>
  ```

### 5.2 `<ol>` (Ordered List)
* **What it does**: Numbered list where sequence matters.
* **Key Attributes**: `type="1|A|a|I|i"`, `start="1"`.
* **Syntax**:
  ```html
  <ol>
    <li>Install Python</li>
    <li>Configure VS Code</li>
    <li>Write your first script</li>
  </ol>
  ```

### 5.3 `<dl>`, `<dt>`, `<dd>` (Description / Glossary List)
* **What it does**: Pairs terms with their definitions (great for FAQs, dictionaries, metadata).
* **Syntax**:
  ```html
  <dl>
    <dt>HTML</dt>
    <dd>HyperText Markup Language for structuring web pages.</dd>
    <dt>CSS</dt>
    <dd>Cascading Style Sheets for styling visual presentations.</dd>
  </dl>
  ```

---

## 6. Data Tables

Tables are used to present structured, tabular data (rows and columns).

* `<table>`: Table wrapper.
* `<caption>`: Descriptive title of the table.
* `<thead>`: Semantic container for the header row.
* `<tbody>`: Semantic container for the main data rows.
* `<tfoot>`: Semantic container for summary/total rows.
* `<tr>`: Table Row.
* `<th>`: Table Header cell (bold and centered by default).
* `<td>`: Table Standard Data cell.

### Complete Table Example:
```html
<table border="1">
  <caption>Student Score Report</caption>
  <thead>
    <tr>
      <th>Roll No</th>
      <th>Student Name</th>
      <th>Subject</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>101</td>
      <td>Aman</td>
      <td>Python</td>
      <td>95</td>
    </tr>
    <tr>
      <td>102</td>
      <td>Sarah</td>
      <td>HTML & CSS</td>
      <td>92</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="3"><strong>Average Score</strong></td>
      <td><strong>93.5</strong></td>
    </tr>
  </tfoot>
</table>
```

---

## 7. Forms & User Inputs

Forms allow users to submit information (login, sign-up, search queries, contact forms) to the server.

### 7.1 `<form>`
* **What it does**: Container for all input fields and submit buttons.
* **Key Attributes**:
  * `action="/submit"`: Server URL to handle data.
  * `method="POST" | "GET"`: HTTP method (`POST` for sensitive/form data, `GET` for searches).

### 7.2 Core Input Types (`<input>`)

```html
<form action="/register" method="POST">
  <!-- Text Input -->
  <label for="username">Username:</label>
  <input type="text" id="username" name="username" placeholder="Enter username" required>

  <!-- Email Input -->
  <label for="user-email">Email Address:</label>
  <input type="email" id="user-email" name="email" placeholder="you@example.com" required>

  <!-- Password Input -->
  <label for="password">Password:</label>
  <input type="password" id="password" name="password" minlength="8" required>

  <!-- Number Input -->
  <label for="age">Age:</label>
  <input type="number" id="age" name="age" min="18" max="100">

  <!-- Date Picker -->
  <label for="dob">Date of Birth:</label>
  <input type="date" id="dob" name="dob">

  <!-- Checkbox (Multiple choices) -->
  <label>
    <input type="checkbox" name="skills" value="python"> Python
  </label>
  <label>
    <input type="checkbox" name="skills" value="html"> HTML5
  </label>

  <!-- Radio Buttons (Single choice only) -->
  <p>Gender:</p>
  <label><input type="radio" name="gender" value="male"> Male</label>
  <label><input type="radio" name="gender" value="female"> Female</label>

  <!-- Dropdown Select Menu -->
  <label for="country">Country:</label>
  <select id="country" name="country">
    <option value="in">India</option>
    <option value="us">United States</option>
    <option value="uk">United Kingdom</option>
  </select>

  <!-- Multi-line Text Area -->
  <label for="message">Your Message:</label>
  <textarea id="message" name="message" rows="4" cols="30" placeholder="Type here..."></textarea>

  <!-- Submit & Reset Buttons -->
  <button type="submit">Submit Registration</button>
  <button type="reset">Clear Form</button>
</form>
```

---

## 8. Interactive & Modern UI Elements

### 8.1 `<details>` & `<summary>` (Native Collapsible Accordion)
* **What it does**: Creates an interactive expandable dropdown widget with zero JavaScript required!
* **Syntax**:
  ```html
  <details>
    <summary>What prerequisites do I need for this course?</summary>
    <p>No prior coding experience is needed. We start from ground zero!</p>
  </details>
  ```

### 8.2 `<dialog>` (Native Modal Pop-up)
* **What it does**: Native browser modal dialog window.
* **Syntax**:
  ```html
  <dialog open>
    <h3>Welcome Alert</h3>
    <p>This is a native HTML5 dialog modal.</p>
  </dialog>
  ```

---

## 9. Block-Level vs. Inline Elements

Understanding how elements behave on the page is essential before learning CSS:

| Category | Behavior | Takes Full Width? | Examples |
| :--- | :--- | :---: | :--- |
| **Block-Level Elements** | Starts on a **new line** and stacks vertically | **Yes** (100% of parent width) | `<div>`, `<header>`, `<main>`, `<footer>`, `<section>`, `<article>`, `<h1>`-`<h6>`, `<p>`, `<ul>`, `<ol>`, `<form>`, `<table>` |
| **Inline Elements** | Sits in the **same line** alongside surrounding text | **No** (Only takes width of its content) | `<span>`, `<a>`, `<strong>`, `<em>`, `<img>`, `<button>`, `<input>`, `<label>`, `<code>`, `<mark>` |

---

## 💡 Summary Cheat Sheet

* Use **`<!DOCTYPE html>`** and standard skeleton for all files.
* Always structure content using **Semantic Tags** (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) instead of endless generic `<div>` tags.
* Always supply meaningful **`alt`** attributes on `<img>` tags.
* Use `<label for="id">` linked with `<input id="id">` for all form fields to ensure accessibility.
