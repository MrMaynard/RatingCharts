# Prerequisites:
* scipy
* numpy
* plotly
* urllib
* flask

# To start server:
`sh server.sh`

# Query string arguments:
* scale: Whether or not to scale the y-axis of the result chart. Defaults to *False*.
* search: The search term to use in chart building. Mandatory.

# Example URL:
`http://127.0.0.1:5000/chart?search=alf&scale=True`
