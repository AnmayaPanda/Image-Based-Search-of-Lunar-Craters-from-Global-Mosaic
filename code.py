from graphviz import Digraph

# Create a Digraph object
dot = Digraph(comment='Use-Case Diagram')

# Define node shapes
dot.node('User', shape='ellipse')
dot.node('UI', 'User Interface', shape='box')
dot.node('PreProc', 'Pre-Processing Module', shape='box')
dot.node('TemplateMatch', 'Template Matching Module', shape='box')
dot.node('DataStorage', 'Data Storage and Retrieval', shape='box')
dot.node('Visualization', 'Visualization Module', shape='box')

# Define edges
dot.edge('User', 'UI', label='Upload Crater Image')
dot.edge('UI', 'PreProc', label='Send Image')
dot.edge('PreProc', 'TemplateMatch', label='Downscaled Image')
dot.edge('TemplateMatch', 'DataStorage', label='Query Crater Location')
dot.edge('TemplateMatch', 'Visualization', label='Send Match Results')
dot.edge('DataStorage', 'TemplateMatch', label='Return Location Data')
dot.edge('Visualization', 'User', label='Display Crater Location')

# Save and render the diagram
dot.render('use_case_diagram', format='png', view=True)
