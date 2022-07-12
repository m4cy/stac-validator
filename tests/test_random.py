"""
Description: Test validation for random sampling

"""
__authors__ = "James Banting", "Jonathan Healy"

from stac_validator import stac_validator

def btest_random(): # basic test
    stac_file = "https://cmr.earthdata.nasa.gov/stac/GES_DISC/collections/M2T1NXSLV"
    stac = stac_validator.StacValidate(stac_file, random=True, sample_number=10, retry=5)
    stac.run()    
    assert len(stac.message) == 10
    assert stac.message == [
        {
            "version": "1.0.0",
            "path": "https://cmr.earthdata.nasa.gov/stac/GES_DISC/collections/M2T1NXSLV.v5.12.4/items/M2T1NXSLV.5.12.4:MERRA2_100.tavg1_2d_slv_Nx.19911207.nc4",
            "schema": [
                "https://schemas.stacspec.org/v1.0.0/item-spec/json-schema/item.json"
            ],
            "valid_stac": True,
            "asset_type": "ITEM",
            "validation_method": "random sample"
        },
        {
            "version": "1.0.0",
            "path": "https://cmr.earthdata.nasa.gov/stac/GES_DISC/collections/M2T1NXSLV.v5.12.4/items/M2T1NXSLV.5.12.4:MERRA2_100.tavg1_2d_slv_Nx.19820404.nc4",
            "schema": [
                "https://schemas.stacspec.org/v1.0.0/item-spec/json-schema/item.json"
            ],
            "valid_stac": True,
            "asset_type": "ITEM",
            "validation_method": "random sample"
        },
        {
            "version": "1.0.0",
            "path": "https://cmr.earthdata.nasa.gov/stac/GES_DISC/collections/M2T1NXSLV.v5.12.4/items/M2T1NXSLV.5.12.4:MERRA2_200.tavg1_2d_slv_Nx.19920123.nc4",
            "schema": [
                "https://schemas.stacspec.org/v1.0.0/item-spec/json-schema/item.json"
            ],
            "valid_stac": True,
            "asset_type": "ITEM",
            "validation_method": "random sample"
        },
        {
            "version": "1.0.0",
            "path": "https://cmr.earthdata.nasa.gov/stac/GES_DISC/collections/M2T1NXSLV.v5.12.4/items/M2T1NXSLV.5.12.4:MERRA2_100.tavg1_2d_slv_Nx.19851003.nc4",
            "schema": [
                "https://schemas.stacspec.org/v1.0.0/item-spec/json-schema/item.json"
            ],
            "valid_stac": True,
            "asset_type": "ITEM",
            "validation_method": "random sample"
        },
        {
            "version": "1.0.0",
            "path": "https://cmr.earthdata.nasa.gov/stac/GES_DISC/collections/M2T1NXSLV.v5.12.4/items/M2T1NXSLV.5.12.4:MERRA2_100.tavg1_2d_slv_Nx.19910711.nc4",
            "schema": [
                "https://schemas.stacspec.org/v1.0.0/item-spec/json-schema/item.json"
            ],
            "valid_stac": True,
            "asset_type": "ITEM",
            "validation_method": "random sample"
        },
        {
            "version": "1.0.0",
            "path": "https://cmr.earthdata.nasa.gov/stac/GES_DISC/collections/M2T1NXSLV.v5.12.4/items/M2T1NXSLV.5.12.4:MERRA2_100.tavg1_2d_slv_Nx.19800609.nc4",
            "schema": [
                "https://schemas.stacspec.org/v1.0.0/item-spec/json-schema/item.json"
            ],
            "valid_stac": True,
            "asset_type": "ITEM",
            "validation_method": "random sample"
        },
        {
            "version": "1.0.0",
            "path": "https://cmr.earthdata.nasa.gov/stac/GES_DISC/collections/M2T1NXSLV.v5.12.4/items/M2T1NXSLV.5.12.4:MERRA2_200.tavg1_2d_slv_Nx.19920326.nc4",
            "schema": [
                "https://schemas.stacspec.org/v1.0.0/item-spec/json-schema/item.json"
            ],
            "valid_stac": True,
            "asset_type": "ITEM",
            "validation_method": "random sample"
        },
        {
            "version": "1.0.0",
            "path": "https://cmr.earthdata.nasa.gov/stac/GES_DISC/collections/M2T1NXSLV.v5.12.4/items/M2T1NXSLV.5.12.4:MERRA2_400.tavg1_2d_slv_Nx.20150504.nc4",
            "schema": [
                "https://schemas.stacspec.org/v1.0.0/item-spec/json-schema/item.json"
            ],
            "valid_stac": True,
            "asset_type": "ITEM",
            "validation_method": "random sample"
        },
        {
            "version": "1.0.0",
            "path": "https://cmr.earthdata.nasa.gov/stac/GES_DISC/collections/M2T1NXSLV.v5.12.4/items/M2T1NXSLV.5.12.4:MERRA2_400.tavg1_2d_slv_Nx.20130801.nc4",
            "schema": [
                "https://schemas.stacspec.org/v1.0.0/item-spec/json-schema/item.json"
            ],
            "valid_stac": True,
            "asset_type": "ITEM",
            "validation_method": "random sample"
        },
        {
            "version": "1.0.0",
            "path": "https://cmr.earthdata.nasa.gov/stac/GES_DISC/collections/M2T1NXSLV.v5.12.4/items/M2T1NXSLV.5.12.4:MERRA2_200.tavg1_2d_slv_Nx.19980719.nc4",
            "schema": [
                "https://schemas.stacspec.org/v1.0.0/item-spec/json-schema/item.json"
            ],
            "valid_stac": True,
            "asset_type": "ITEM",
            "validation_method": "random sample"
        }
    ]

def btest_lower_bounds_random(): # edge sample test
    stac_file = "https://cmr.earthdata.nasa.gov/stac/GES_DISC/collections/M2T1NXSLV"
    stac = stac_validator.StacValidate(stac_file, random=True, sample_number=1, retry=5)
    stac.run()    
    assert len(stac.message) == 1
    assert stac.message == [
    {
        "version": "1.0.0",
        "path": "https://cmr.earthdata.nasa.gov/stac/GES_DISC/collections/M2T1NXSLV.v5.12.4/items/M2T1NXSLV.5.12.4:MERRA2_100.tavg1_2d_slv_Nx.19911207.nc4",
        "schema": [
            "https://schemas.stacspec.org/v1.0.0/item-spec/json-schema/item.json"
        ],
        "valid_stac": True,
        "asset_type": "ITEM",
        "validation_method": "random sample"
    }
]

def btest_zero_samples_random(): # edge sample test
    stac_file = "https://cmr.earthdata.nasa.gov/stac/GES_DISC/collections/M2T1NXSLV"
    stac = stac_validator.StacValidate(stac_file, random=True, sample_number=0, retry=5)
    stac.run()    
    assert len(stac.message) == 1
    assert stac.message == [
        {
            "version": "1.0.0",
            "path": "https://cmr.earthdata.nasa.gov/stac/GES_DISC/collections/M2T1NXSLV",
            "schema": [
                ""
            ],
            "valid_stac": False,
            "error_type": "ValueError",
            "error_message": "Sample number must be between 1 and 500."
        }
    ]

def test_collection_limit_bounds_random(): # test when sample number is greater than actual number of granules
    stac_file = "https://cmr.earthdata.nasa.gov/stac/LANCEMODIS/collections/VNP14IMGTDL_NRT"
    stac = stac_validator.StacValidate(stac_file, random=True, sample_number=10, retry=5)
    stac.run()
    assert len(stac.message) == 8
