import java.util.Deque;

class Trie
{
    public Trie[] children;
    public boolean isEnd;

    public Trie()
    {
        isEnd = false;
        children = new Trie[26];
    }

    public void insert(String word)
    {
        Trie node = this;
        for(char ch: word.toCharArray())
        {
            if(node.children[ch - 'a'] == null)
                node.children[ch - 'a'] = new Trie();
            node = node.children[ch - 'a'];
        }
        node.isEnd = true;
    }

    public boolean search(Deque<Character> word)
    {
        Trie node = this;
        for(char ch: word)
        {
            if(node.children[ch - 'a'] == null) return false;
            node = node.children[ch - 'a'];
        }
        return isEnd;
    }
}

class StreamChecker
{
    public Trie node = new Trie();
    public Deque<Character> stream = new LinkedList();

    public StreamChecker(String[] words) {
        for(String w: words)
        {
            String w_rev = new StringBuilder(w).reverse().toString();
            node.insert(w_rev);
        }
    }
    
    public boolean query(char letter) {
        stream.addFirst(letter);
        return node.search(stream);
    }
}

class Main
{
    public static void main(String[] args)
    {
        String word = "datastructure";      // there should not be any space or capital letter
        String prefix = "data";
        String del = "data";
        Trie s = new Trie();
        s.insert(word);
        System.out.println("search: " + s.search(word));    // only whole 'word' can give result true
        System.out.println("start with: " + s.startWith(prefix));    // any no. of chars can give true result but it must start as in 'word'
        s.delete(del);
        s.display(word);
    }
}
