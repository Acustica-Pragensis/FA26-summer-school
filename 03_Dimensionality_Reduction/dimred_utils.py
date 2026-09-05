import numpy as np
import re

def load_comsol_export(filepath):
    """
    Loads COMSOL 2D table exports using pure NumPy.
    Extracts timestamps from the header and drops inactive domain points (NaN rows).
    
    Returns:
        coords     : np.ndarray of shape (N_points, 2) -> [X, Y]
        time_array : np.ndarray of shape (N_timesteps,) -> time values [s]
        snapshots  : np.ndarray of shape (N_points, N_timesteps) -> snapshot matrix X
    """
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    # Locate header line containing '% X,Y,...'
    header_idx = None
    for idx, line in enumerate(lines):
        if re.search(r'%\s*X\s*,\s*Y', line, re.IGNORECASE):
            header_idx = idx
            break
            
    if header_idx is None:
        raise ValueError(f"Could not find the header row '% X,Y...' in {filepath}")
    
    # Extract timestamps from the column headers
    header_line = lines[header_idx].lstrip('%').strip()
    headers = [h.strip() for h in header_line.split(',')]
    time_headers = headers[2:]
    
    time_list = []
    for h in time_headers:
        match = re.search(r't=([\d\.eE\+-]+)', h)
        time_list.append(float(match.group(1)) if match else np.nan)
    time_array = np.array(time_list, dtype=np.float64)
    
    # Load numerical data directly using NumPy
    raw_data = np.genfromtxt(filepath, delimiter=',', skip_header=header_idx + 1, dtype=np.float64)
    
    coords_all = raw_data[:, :2]
    snapshots_all = raw_data[:, 2:]
    
    # Filter out inactive grid points outside the room boundary (all-NaN rows)
    valid_mask = ~np.isnan(snapshots_all).all(axis=1)
    
    coords = coords_all[valid_mask]
    snapshots = snapshots_all[valid_mask]
    
    return coords, time_array, snapshots