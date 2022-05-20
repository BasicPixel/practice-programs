function App() {
  const [quote, setQuote] = React.useState(null);
  const [uriQuote, setUriQuote] = React.useState(null);

  const fetchQuote = () => {
    const url = 'https://programming-quotes-api.herokuapp.com/Quotes/random';
    fetch(url)
      .then((res) => res.json())
      .then((data) => {
        setQuote(data);
        setUriQuote(encodeURIComponent('"' + data.en + '" ' + data.author));
      });
  };

  React.useEffect(() => {
    fetchQuote();
  }, []);

  return (
    <>
      <div id="quote-box">
        <h2 id="text">{quote ? quote.en : 'Loading...'}</h2>
        <p id="author">{quote ? `- ${quote.author}` : ''}</p>
        <button id="new-quote" onClick={fetchQuote}>
          New Quote
        </button>
        <a
          href={`https://twitter.com/intent/tweet?text=${uriQuote}`}
          target="_blank"
          rel="noreferrer noopener"
          id="tweet-quote"
        >
          <button>Tweet</button>
        </a>
      </div>
    </>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
