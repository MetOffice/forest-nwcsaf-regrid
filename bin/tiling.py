"""Wrap forest.geo to make an easier interface"""
import numpy as np
import geo


def web_mercator(lons, lats):
    """Similar to forest.geo.web_mercator but preserves array shape"""
    if (lons.ndim == 1):
        gx, _ = geo.web_mercator(
            lons,
            np.zeros(len(lons), dtype="d"))
        _, gy = geo.web_mercator(
            np.zeros(len(lats), dtype="d"),
            lats)
        return gx, gy
    elif (lons.ndim == 2) and (lats.ndim == 2):
        gx, gy = geo.web_mercator(lons, lats)
        gx = gx.reshape(lons.shape)
        gx = np.ma.masked_invalid(gx)
        gy = gy.reshape(lats.shape)
        gy = np.ma.masked_invalid(gy)
        return gx, gy
    else:
        raise Exception("Either 1D or 2D lons/lats")
