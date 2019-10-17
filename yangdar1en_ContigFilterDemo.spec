/*
A KBase module: yangdar1en_ContigFilterDemo
This sample module contains one small method that filters contigs.
*/

module yangdar1en_ContigFilterDemo {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_yangdar1en_ContigFilterDemo(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;
    funcdef run_yangdar1en_ContigFilterDemo_max(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;
};
