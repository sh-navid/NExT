class Mermaid:
    @staticmethod
    def script():
        return """
            <script 
                src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.9.0/mermaid.min.js" 
                integrity="sha512-gx05X612uoaolzJ5Ee/786b3th+qzAm90TOvRwZJwnE8yr0sHQG8eLxdR0/Hbqc2IFh2mWHzzXk79g3atNSwsQ==" 
                crossorigin="anonymous" 
                referrerpolicy="no-referrer">
            </script>
        """

    class Chart:
        @staticmethod
        def graph(edges):  # [["A","B"], ["B","C"], ["B","D"]]
            mermaid = """
                <pre class="mermaid">
                    graph
                    [GRAPH]
                </pre>
            """

            taboo = []
            graph = ""

            for edge in edges:
                token = f"{edge[0]} --> {edge[1]}\n"
                if token not in taboo:
                    graph += token
                    taboo.append(token)

            mermaid = mermaid.replace("[GRAPH]", graph)
            return mermaid
