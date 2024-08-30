import streamlit as st
import json

# Define the graph data (nodes and links)
graph_data = {
    "nodes": [
        {"id": "A", "group": 1},
        {"id": "B", "group": 1},
        {"id": "C", "group": 1},
        {"id": "D", "group": 2},
        {"id": "E", "group": 2},
    ],
    "links": [
        {"source": "A", "target": "B", "value": 1, "label": "A-B"},
        {"source": "A", "target": "C", "value": 1, "label": "A-C"},
        {"source": "B", "target": "D", "value": 1, "label": "B-D"},
        {"source": "C", "target": "E", "value": 1, "label": "C-E"},
    ]
}

# Convert the graph data to JSON
graph_json = json.dumps(graph_data)

# Streamlit app layout
st.title("Graph Visualization with D3.js")

# Create the HTML for D3.js visualization
html_code = f"""
<!DOCTYPE html>
<meta charset="utf-8">
<style>
    .node {{
        stroke: #fff;
        stroke-width: 1.5px;
    }}

    .link {{
        stroke: #999;
        stroke-opacity: 0.6;
    }}

    .label {{
        font-family: Arial, sans-serif;
        font-size: 12px;
        fill: #000;
        pointer-events: none;
    }}
</style>
<body>
<script src="https://d3js.org/d3.v6.min.js"></script>
<script>

    var graph = {graph_json};

    var width = 600;
    var height = 400;

    var svg = d3.select("body").append("svg")
        .attr("width", width)
        .attr("height", height);

    var simulation = d3.forceSimulation(graph.nodes)
        .force("link", d3.forceLink(graph.links).id(d => d.id).distance(200))
        .force("charge", d3.forceManyBody().strength(-400))
        .force("center", d3.forceCenter(width / 2, height / 2));

    var link = svg.append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(graph.links)
        .enter().append("line")
        .attr("class", "link")
        .attr("stroke-width", d => Math.sqrt(d.value));

    var linkLabels = svg.append("g")
        .attr("class", "link-labels")
        .selectAll(".link-label")
        .data(graph.links)
        .enter().append("text")
        .attr("class", "label")
        .attr("dy", -5)
        .text(d => d.label);

    var node = svg.append("g")
        .attr("class", "nodes")
        .selectAll("circle")
        .data(graph.nodes)
        .enter().append("circle")
        .attr("class", "node")
        .attr("r", 10)
        .attr("fill", d => d.group == 1 ? "red" : "blue")
        .call(d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended));

    var nodeLabels = svg.append("g")
        .attr("class", "node-labels")
        .selectAll(".node-label")
        .data(graph.nodes)
        .enter().append("text")
        .attr("class", "label")
        .attr("dy", -10)
        .attr("dx", 12)
        .text(d => d.id);

    simulation
        .nodes(graph.nodes)
        .on("tick", ticked);

    simulation.force("link")
        .links(graph.links);

    function ticked() {{
        link
            .attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);

        linkLabels
            .attr("x", d => (d.source.x + d.target.x) / 2)
            .attr("y", d => (d.source.y + d.target.y) / 2);

        node
            .attr("cx", d => d.x)
            .attr("cy", d => d.y);

        nodeLabels
            .attr("x", d => d.x)
            .attr("y", d => d.y);
    }}

    function dragstarted(event, d) {{
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
    }}

    function dragged(event, d) {{
        d.fx = event.x;
        d.fy = event.y;
    }}

    function dragended(event, d) {{
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
    }}

</script>
</body>
"""

# Render the D3.js graph in Streamlit using an HTML component
st.components.v1.html(html_code, height=450)
