import streamlit as st
import streamlit.components.v1 as components

# Title of the app
st.title("Interactive Knowledge Graph Visualization")

# Description
st.write("This is a simple interactive knowledge graph visualization using D3.js in a Streamlit app.")

# D3.js visualization
components.html("""
<div id="graph-container"></div>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
// Define the graph data (nodes and links)
var nodes = [
    {id: "Person", group: 1},
    {id: "Alice", group: 2},
    {id: "Bob", group: 2},
    {id: "Company", group: 1},
    {id: "Acme Corp", group: 3},
    {id: "Wonderland Ltd", group: 3}
];

var links = [
    {source: "Alice", target: "Person", value: 1},
    {source: "Bob", target: "Person", value: 1},
    {source: "Alice", target: "Acme Corp", value: 1},
    {source: "Bob", target: "Wonderland Ltd", value: 1},
    {source: "Acme Corp", target: "Company", value: 1},
    {source: "Wonderland Ltd", target: "Company", value: 1}
];

// Setup the SVG canvas dimensions
var width = 600, height = 400;

var svg = d3.select("#graph-container").append("svg")
    .attr("width", width)
    .attr("height", height);

// Initialize the simulation
var simulation = d3.forceSimulation(nodes)
    .force("link", d3.forceLink(links).id(d => d.id).distance(100))
    .force("charge", d3.forceManyBody().strength(-200))
    .force("center", d3.forceCenter(width / 2, height / 2));

// Create links
var link = svg.append("g")
    .attr("class", "links")
  .selectAll("line")
  .data(links)
  .enter().append("line")
    .attr("stroke-width", d => Math.sqrt(d.value))
    .attr("stroke", "#999");

// Create nodes
var node = svg.append("g")
    .attr("class", "nodes")
  .selectAll("circle")
  .data(nodes)
  .enter().append("circle")
    .attr("r", 10)
    .attr("fill", d => {
        if (d.group === 1) return "#ffab00";  // Yellow for entity types
        else if (d.group === 2) return "#1f77b4";  // Blue for people
        else return "#2ca02c";  // Green for companies
    })
    .call(d3.drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended));

// Add labels to nodes
var labels = svg.append("g")
    .attr("class", "labels")
  .selectAll("text")
  .data(nodes)
  .enter().append("text")
    .attr("dy", -15)
    .attr("text-anchor", "middle")
    .attr("font-size", 12)
    .text(d => d.id);

// Define the zoom behavior
svg.call(d3.zoom()
    .extent([[0, 0], [width, height]])
    .scaleExtent([1, 8])
    .on("zoom", zoomed));

function zoomed({transform}) {
    svg.attr("transform", transform);
}

// Define the drag behaviors
function dragstarted(event, d) {
  if (!event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(event, d) {
  d.fx = event.x;
  d.fy = event.y;
}

function dragended(event, d) {
  if (!event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}

// Update simulation on every tick
simulation.on("tick", () => {
  link
      .attr("x1", d => d.source.x)
      .attr("y1", d => d.source.y)
      .attr("x2", d => d.target.x)
      .attr("y2", d => d.target.y);

  node
      .attr("cx", d => d.x)
      .attr("cy", d => d.y);

  labels
      .attr("x", d => d.x)
      .attr("y", d => d.y);
});
</script>
""", height=500)
