import streamlit as st
import streamlit.components.v1 as components

# Title of the app
st.title("End-to-End LLMOps Flow Visualization")

# LLMOps Flow Visualization
st.header("LLMOps Flow Visualization")
components.html("""
<div id="llmops-flow"></div>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
// LLMOps Flow Data
var data = {
  "nodes": [
    {"id": "GPT-4", "group": 1},
    {"id": "OpenAI", "group": 2},
    {"id": "Hugging Face", "group": 3},
    {"id": "AWS Sagemaker", "group": 4},
    {"id": "Pinecone", "group": 5},
    {"id": "Neo4j", "group": 6},
    {"id": "Vespa", "group": 7},
    {"id": "Prometheus", "group": 8},
    {"id": "GitHub Actions", "group": 9}
  ],
  "links": [
    {"source": "GPT-4", "target": "OpenAI", "value": 1, "name": "used by"},
    {"source": "GPT-4", "target": "Hugging Face", "value": 1, "name": "fine-tuned on"},
    {"source": "GPT-4", "target": "AWS Sagemaker", "value": 1, "name": "deployed on"},
    {"source": "GPT-4", "target": "Pinecone", "value": 1, "name": "indexes in"},
    {"source": "GPT-4", "target": "Neo4j", "value": 1, "name": "indexes in"},
    {"source": "Vespa", "target": "Pinecone", "value": 1, "name": "integrates with"},
    {"source": "Vespa", "target": "Neo4j", "value": 1, "name": "integrates with"},
    {"source": "AWS Sagemaker", "target": "Prometheus", "value": 1, "name": "monitored by"},
    {"source": "AWS Sagemaker", "target": "GitHub Actions", "value": 1, "name": "managed by"}
  ]
};

// D3.js Visualization
var width = 600, height = 400;

var svg = d3.select("#llmops-flow").append("svg")
    .attr("width", width)
    .attr("height", height);

var simulation = d3.forceSimulation(data.nodes)
    .force("link", d3.forceLink(data.links).id(d => d.id).distance(100))
    .force("charge", d3.forceManyBody().strength(-400))
    .force("center", d3.forceCenter(width / 2, height / 2));

// Add lines for links
var link = svg.append("g")
    .attr("class", "links")
  .selectAll("line")
  .data(data.links)
  .enter().append("line")
    .attr("stroke-width", d => Math.sqrt(d.value))
    .attr("stroke", "#999");

// Add labels for links
var linkLabels = svg.append("g")
    .attr("class", "link-labels")
  .selectAll("text")
  .data(data.links)
  .enter().append("text")
    .attr("font-size", 10)
    .attr("fill", "#555")
    .text(d => d.name);

// Add circles for nodes
var node = svg.append("g")
    .attr("class", "nodes")
  .selectAll("circle")
  .data(data.nodes)
  .enter().append("circle")
    .attr("r", 10)
    .attr("fill", "#69b3a2")
    .call(d3.drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended));

// Add labels for nodes
var nodeLabels = svg.append("g")
    .attr("class", "node-labels")
  .selectAll("text")
  .data(data.nodes)
  .enter().append("text")
    .attr("font-size", 12)
    .attr("dy", -15)
    .attr("text-anchor", "middle")
    .text(d => d.id);

// Update positions
simulation.on("tick", () => {
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
});

// Drag functions
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
</script>
""", height=400)
