# IoT Dashboard Design with Dash

Sample example to use Dash python framework for IoT Dashboard Design

"Dash is a Python framework for building analytical web applications. No JavaScript required. Build on top of Plotly.js, React, and Flask, Dash ties modern UI elements like dropdowns, sliders, and graphs directly to your analytical python code." ..._from [Dash by plotly](https://plot.ly/products/dash/)_

See more on [Dash Gallery](https://dash.plot.ly/gallery)

## Example 1. Chart Display 

 Started with the first example from [Dash User Guide](https://dash.plot.ly/getting-started), set an interval value (3 secs) and defined callbacks. 

<p align="center">
<img src="https://github.com/phyunsj/iot-dashboard-design-with-dash/blob/master/images/node-red-example1.gif" width="500px"/>
</p
 
 `index.html`, `_dash-layout`, `_dash-dependencies` were generated by Dash framework. Use it directly for Node-RED `template` node. For live-update, serve `_dash-update-component` POST request.

<p align="center">
<img src="https://github.com/phyunsj/iot-dashboard-design-with-dash/blob/master/images/dash-example1.png" width="500px"/>
</p>

 ```
 [{"id":"abd033f5.78c24","type":"http response","z":"45713e9d.6607c","name":"http response","statusCode":"","headers":{},"x":918,"y":106,"wires":[]},{"id":"724d7b54.5e8ee4","type":"http in","z":"45713e9d.6607c","name":"","url":"/chart","method":"get","upload":false,"swaggerDoc":"","x":91,"y":78,"wires":[["4492d7dd.4e0a18"]]},{"id":"14ce7f19.c52c81","type":"http in","z":"45713e9d.6607c","name":"","url":"/_dash-layout","method":"get","upload":false,"swaggerDoc":"","x":120,"y":118,"wires":[["9707cf45.c8f5"]]},{"id":"b5cbb71f.b47c58","type":"http in","z":"45713e9d.6607c","name":"","url":"/_dash-dependencies","method":"get","upload":false,"swaggerDoc":"","x":140,"y":157,"wires":[["33bb202e.b7161"]]},{"id":"d9f8406c.523ba","type":"http in","z":"45713e9d.6607c","name":"","url":"/_dash-update-component","method":"post","upload":false,"swaggerDoc":"","x":161,"y":199,"wires":[["59b51916.f9cd18"]]},{"id":"5597ab59.f5c374","type":"change","z":"45713e9d.6607c","name":"Set Headers","rules":[{"t":"set","p":"headers","pt":"msg","to":"{}","tot":"json"},{"t":"set","p":"headers.content-type","pt":"msg","to":"application/json","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":655,"y":147,"wires":[["abd033f5.78c24"]]},{"id":"9707cf45.c8f5","type":"template","z":"45713e9d.6607c","name":"_dash-layout","field":"payload","fieldType":"msg","format":"handlebars","syntax":"mustache","template":"{\"type\": \"Div\", \"namespace\": \"dash_html_components\", \"props\": {\"children\": [{\"type\": \"H1\", \"namespace\": \"dash_html_components\", \"props\": {\"children\": \"Hello Dash\"}}, {\"type\": \"Div\", \"namespace\": \"dash_html_components\", \"props\": {\"children\": \"\\n        Dash: Node-RED Example\\n    \"}}, {\"type\": \"Graph\", \"namespace\": \"dash_core_components\", \"props\": {\"id\": \"example-graph\", \"figure\": {\"data\": [{\"y\": [4, 1, 2], \"x\": [1, 2, 3], \"type\": \"bar\", \"name\": \"SF\"}, {\"y\": [2, 4, 5], \"x\": [1, 2, 3], \"type\": \"bar\", \"name\": \"Montreal\"}], \"layout\": {\"title\": \"Dash Data Visualization\"}}}}, {\"type\": \"Interval\", \"namespace\": \"dash_core_components\", \"props\": {\"interval\": 3000, \"id\": \"graph-update\", \"n_intervals\": 0}}]}}","output":"json","x":384,"y":117,"wires":[["5597ab59.f5c374"]]},{"id":"33bb202e.b7161","type":"template","z":"45713e9d.6607c","name":"_dash-dependencies","field":"payload","fieldType":"msg","format":"handlebars","syntax":"mustache","template":"[{\"events\":[],\"inputs\":[{\"id\":\"graph-update\",\"property\":\"n_intervals\"}],\"output\":{\"id\":\"example-graph\",\"property\":\"figure\"},\"state\":[]}]\n","output":"json","x":410,"y":158,"wires":[["5597ab59.f5c374"]]},{"id":"4492d7dd.4e0a18","type":"template","z":"45713e9d.6607c","name":"index.html","field":"payload","fieldType":"msg","format":"handlebars","syntax":"mustache","template":"<!DOCTYPE html>\n<html>\n    <head>\n        <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n      <meta charset=\"UTF-8\">\n        <title>Dash</title>\n        <link rel=\"stylesheet\" href=\"https://codepen.io/chriddyp/pen/bWLwgP.css\">\n<link rel=\"stylesheet\" href=\"https://unpkg.com/react-select@1.0.0-rc.3/dist/react-select.min.css\">\n<link rel=\"stylesheet\" href=\"https://unpkg.com/react-virtualized@9.9.0/styles.css\">\n<link rel=\"stylesheet\" href=\"https://unpkg.com/react-virtualized-select@3.1.0/styles.css\">\n<link rel=\"stylesheet\" href=\"https://unpkg.com/rc-slider@6.1.2/assets/index.css\">\n<link rel=\"stylesheet\" href=\"https://unpkg.com/dash-core-components@0.34.0/dash_core_components/react-dates@12.3.0.css\">\n    </head>\n    <body>\n        \n<div id=\"react-entry-point\">\n    <div class=\"_dash-loading\">\n        Loading...\n    </div>\n</div>\n\n        <footer>\n            <script id=\"_dash-config\" type=\"application/json\">{\"requests_pathname_prefix\": \"/\", \"url_base_pathname\": null}</script>\n            <script src=\"https://unpkg.com/react@15.4.2/dist/react.min.js\"></script>\n<script src=\"https://unpkg.com/react-dom@15.4.2/dist/react-dom.min.js\"></script>\n<script src=\"https://unpkg.com/dash-html-components@0.13.2/dash_html_components/dash_html_components.min.js\"></script>\n<script src=\"https://cdn.plot.ly/plotly-1.41.3.min.js\"></script>\n<script src=\"https://unpkg.com/dash-core-components@0.34.0/dash_core_components/dash_core_components.min.js\"></script>\n<script src=\"https://unpkg.com/dash-renderer@0.14.3/dash_renderer/dash_renderer.min.js\"></script>\n        </footer>\n    </body>\n</html>","output":"str","x":384,"y":78,"wires":[["abd033f5.78c24"]]},{"id":"d012aba6.cc3678","type":"debug","z":"45713e9d.6607c","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"false","x":656,"y":196,"wires":[]},{"id":"59b51916.f9cd18","type":"function","z":"45713e9d.6607c","name":"generate Trace","func":"msg.payload = { response: {props: {figure: { data : [], layout : {} }}}};\n\nmsg.payload.response.props.figure.data = [{\"y\": [Math.floor(Math.random() * 4) + 1 , Math.floor(Math.random() * 4) + 1, Math.floor(Math.random() * 4) + 1], \"x\": [1,2,3], \"type\": \"bar\", \"name\": \"SF\"}, {\"y\": [Math.floor(Math.random() * 4) + 1, Math.floor(Math.random() * 4) + 1, Math.floor(Math.random() * 4) + 1], \"x\": [1,2,3], \"type\": \"bar\", \"name\": \"Montreal\"}];\nmsg.payload.response.props.figure.layout = {\"title\": \"Dash Data Visualization\"};\n\nreturn msg;","outputs":1,"noerr":0,"x":393,"y":198,"wires":[["d012aba6.cc3678","5597ab59.f5c374"]]}]
 ```

## Example 2. TBD

### Other Consideration

[shinydashboard for R](https://rstudio.github.io/shinydashboard/index.html)
