from .common import DOIInfo, default_doi_resolver, CT

class DataciteDOIInfo(DOIInfo):
    """
    a specialization of DOIInfo for Datacite DOIs.  This specialization knows
    how to retrieve the native DOI metadata.
    """

    def __init__(self, doi, source="Datacite", resolver=default_doi_resolver,
                 logger=None):
        super(DataciteDOIInfo, self).__init__(doi, source, resolver, logger)

    @property
    def native(self):
        """
        DOI metadata in the schema specific to the registration agency--in 
        this case, Datacite.
        """
        if self._native is None:
            self._native=self._get_data(CT.Datacite_JSON, "json")
        return self._native

