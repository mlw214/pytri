#!/usr/bin/env python3

from IPython.display import Javascript, HTML, display
import requests
import uuid
import json

import networkx as nx
from networkx.readwrite import json_graph

print("blah")

__version__ = "0.0.1"


class pytri:

    def __init__(self):
        scripts = [
            "https://threejs.org/examples/js/controls/TrackballControls.js",
        ]

        threesrc = requests.get("https://threejs.org/build/three.js").text.split('\n')
        threesrc = threesrc[6:-2]

        js = "exports = window.THREE || {}; " + "\n".join(threesrc) + "window.THREE = exports;"

        for script in scripts:
            js += requests.get(script).text.strip()

        with open("./substrate.min.js", 'r') as fh:
            js += ";\n\n" + fh.read().strip()

        self.js = js
        self.uid = str(uuid.uuid4())

    def show(self):
        display(HTML("<script>{}</script>".format(self.js) + 
            "<div id='pytri-target-{}'></div>".format(self.uid) + """
            <script>
            V = {}
            V['"""+self.uid+"""'] = new Visualizer({
                targetElement: "pytri-target-"""+self.uid+"""",
                backgroundColor: new window.THREE.Color(0xffffff),
                renderLayers: {
                    // None yet!
                }
            });
            V['"""+self.uid+"""'].triggerRender();
            V['"""+self.uid+"""'].resize(undefined, 400)
            </script>
        """))

    def remove_layer(self, name):
        display(Javascript("""
            V['"""+self.uid+"""'].removeLayer('{}')
        """.format(name)))

    def axes(self):
        display(Javascript("""
            class AxisLayer extends Layer {
                requestInit(scene) {
                    let axes = new window.THREE.AxisHelper(5);
                    this.children.push(axes)
                    scene.add(axes)
                }
            }
            V['"""+self.uid+"""'].addLayer('axes', new AxisLayer())
        """))

    def scatter(self, data, r=0.15, c=0x00babe):
        _js = ("""
        class ScatterLayer extends Layer {
            constructor(opts) {
                super(opts);

                this.setData = this.setData.bind(this);
                this.radius = opts.radius || 0.15;
                this.colors = opts.colors || 0x00babe;
                if (typeof(this.colors) == "number") {
                    this.c_array = false;
                } else {
                    this.c_array = true;
                }
                this.setData(opts.data);
            }

            setData(data) {
                this.data = data;
                this.requestInit;
            }

            requestInit(scene) {
                for (let i = 0; i < this.data.length; i++) {
                    let sph = new window.THREE.Mesh(
                        new window.THREE.SphereGeometry(this.radius, 6, 6),
                        new window.THREE.MeshBasicMaterial({
                            color: this.c_array ? this.colors[i] : this.colors
                        })
                    );
                    sph.position.set(...this.data[i]);
                    this.children.push(sph)
                    scene.add(sph)
                    
                }
            }
        }
        """ + """
        V['"""+self.uid+"""'].addLayer('scatter', new ScatterLayer({{
            data: {},
            radius: {},
            colors: {}
        }}))
        """.format(
            json.dumps(data),
            r,
            c
        ))
        display(Javascript(_js))


    def graph(self, data, r=0.15, c=0xbabe00):
        if isinstance(data, nx.Graph):
            data = json_graph.node_link_data(data)

        print(data)
        _js = ("""
        class GraphLayer extends Layer {
            constructor(opts) {
                super(opts);

                this.setData = this.setData.bind(this);
                this.radius = opts.radius || 0.15;
                this.colors = opts.colors || 0x00babe;
                if (typeof(this.colors) == "number") {
                    this.c_array = false;
                } else {
                    this.c_array = true;
                }
                this.setData(opts.data);
            }

            setData(data) {
                this.data = data;
                this.requestInit;
            }

            requestInit(scene) {
                for (let i = 0; i < this.data.nodes.length; i++) {
                    let sph = new window.THREE.Mesh(
                        new window.THREE.SphereGeometry(this.radius, 6, 6),
                        new window.THREE.MeshBasicMaterial({
                            color: this.c_array ? this.colors[i] : this.colors
                        })
                        );
                    sph.position.set(...this.data.nodes[i].pos);
                    this.children.push(sph)
                    scene.add(sph)
                }

                for (var i = 0; i < this.data.links.length; i++) {
                    var edgeGeometry = new window.THREE.Geometry();
                    var edgeMaterial = new window.THREE.LineBasicMaterial({
                        color: 0xbabe00 * (this.data.links[i].weight || 1),
                        transparent: true,
                        opacity: this.data.links[i].weight || 1,
                        linewidth: this.data.links[i].weight || 1,
                    });
                    edgeGeometry.vertices.push(
                        new window.THREE.Vector3(...this.data.nodes[this.data.links[i].source].pos),
                        new window.THREE.Vector3(...this.data.nodes[this.data.links[i].target].pos)
                        );

                    var line = new window.THREE.Line(edgeGeometry, edgeMaterial);
                    this.children.push(line);
                    scene.add(line);
                }
            }
        }
        """ + """
        V['"""+self.uid+"""'].addLayer('graph', new GraphLayer({{
            data: {},
            radius: {},
            colors: {}
        }}))
        """.format(
            json.dumps(data),
            r,
            c
        ))
        display(Javascript(_js))


