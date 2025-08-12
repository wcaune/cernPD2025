import h5py as h5
import plotly.graph_objects as go

# Load the point cloud data from the HDF5 file
entry = 0
with h5.File('example_xyze_100.h5','r') as f:
    print(len(f['data']),'images found')
    # read the specified entry
    pts=f['data'][entry].reshape(-1,4)

print('Visualizing entry',entry)
d=go.Scatter3d(x=pts[:,0],y=pts[:,1],z=pts[:,2], mode='markers', marker=dict(size=2))

fig = go.Figure(data=[d])
fig.update_layout(width=1200, height=800)
fig.show()

# 2nd
import h5py as h5
import plotly.graph_objects as go

# Load the point cloud data from the HDF5 file
with h5.File('example_label_100.h5','r') as f:
    # read the specified entry
    labels=f['labels'][entry]

print('Visualizing labels for entry',entry)
d=go.Scatter3d(x=pts[:,0],y=pts[:,1],z=pts[:,2], mode='markers', marker=dict(size=2,color=labels))

fig = go.Figure(data=[d])
fig.update_layout(width=1200, height=800)
fig.show()

# 3rd : The image typically contains lots of scattered low energy depositions. They can be easily identified by a semabtic label value of 4. Let's clean up the images by:
# Adding energy for each point with a color scale
# Masking low energy scattering points

import numpy as np 

# Create a mask to filter out the semantic type 4 (which is the max value, so can just use "<4").
mask=labels < 4

# Apply the mask to pts and labels
sub_pts=pts[mask]
sub_labels=labels[mask]

# Visualize the filtered points. Some decoration also done to make it look better.
d=go.Scatter3d(x=sub_pts[:,0],y=sub_pts[:,1],z=sub_pts[:,2], mode='markers', 
               marker=dict(color=np.log10(sub_pts[:,3]),
                           size=np.log10(sub_pts[:,3]*1000).astype(int)+1,
                           colorscale='viridis',
                           opacity=0.7, 
                           line=dict(width=0),
                           ),
                hovertext=[f'{sub_pts[i,3]} MeV' for i in range(len(sub_pts))],
               )
fig = go.Figure(data=[d])
fig.update_layout(width=1200, height=800,                  
                  scene=dict(
                    xaxis=dict(nticks=4, range=[0, 767]),
                    yaxis=dict(nticks=4, range=[0, 767]),
                    zaxis=dict(nticks=4, range=[0, 767]),
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Z',
                    aspectmode='cube'),
                  title='3D Scatter Plot of xyze')
fig.show()

# Visualize the filtered points with labels
d=go.Scatter3d(x=sub_pts[:,0],y=sub_pts[:,1],z=sub_pts[:,2], mode='markers', 
               marker=dict(color=sub_labels,
                           size=np.log10(sub_pts[:,3]*1000).astype(int)+1,
                           colorscale='viridis',
                           opacity=0.7,
                           line=dict(width=0)),
               hovertext=labels,
               )
fig = go.Figure(data=[d])
fig.update_layout(width=1200, height=800,
                  
                  scene=dict(
                    xaxis=dict(nticks=4, range=[0, 767]),
                    yaxis=dict(nticks=4, range=[0, 767]),
                    zaxis=dict(nticks=4, range=[0, 767]),
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Z',
                    aspectmode='cube'),
                  title='3D Scatter Plot ofLabels')
fig.show()



