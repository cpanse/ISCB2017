#!/usr/bin/python

"""
Christian Panse <cp@fgcz.ethz.ch> 2017
code to annotate blasted FASTA
"""
import os
import json
import re

import sys
import getopt

import yaml

class FgczBlastp:
    """
    reads json files generated by blastp and annotated a fasta file with search results


    """
    queryEvalueDict = dict()
    queryDict = dict()
    alternativeDict = dict()
    swissprotid_pattern = "^([a-z]{2}[|_A-Z0-9]+)\ .*$"
    swissprotid_regex = re.compile(swissprotid_pattern)
    fastaregex = re.compile(">([-|\._\w]+)\s+.+$")

    blast_cutoff_evalue = 1E-6
    blast_cutoff_evalue = 1

    def extract1sthit(self, f):
        fastaregex = re.compile("([-|\._\w]+)\s+.+$")
        try:
            with open(f) as data_file:
                data = json.load(data_file)
        except:
            return
        try:
            query = data["BlastOutput2"]["report"]["results"]["search"]["query_title"]
            res = fastaregex.match(query)
            query = res.group(1)

        except:
            return

        evalue = None
        title = None

        try:
            x = data["BlastOutput2"]["report"]["results"]["search"]["hits"][0]

            evalue = x["hsps"][0]["evalue"]
            title = x["description"][0]["title"]

        except:
            pass

        try:
            x = data["BlastOutput2"]["report"]["results"]["search"]["hits"]

            n = len(x)

            self.alternativeDict[query] = map(lambda idx: {'evalue': x[idx]["hsps"][0]["evalue"], 'title': x[idx]["description"][0]["title"]},
                                           range(0, n))

        except:
            pass

        try:
            res = self.swissprotid_regex.match(title)
            title = res.group(1)
        except:
            pass

        if evalue < self.blast_cutoff_evalue:
            #print "DEBUG {}\t{}\t{}".format(evalue, query, title)
            self.queryDict[query] = title
            self.queryEvalueDict[query] = evalue

    def scan(self, path='.', pattern="PigeonPea_[0-9]+\.json"):
        mypath = path
        regex = re.compile(pattern)

        files = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

        for i in filter(regex.match, files):
            self.extract1sthit(i)


    def write_yaml(self, yaml_filename='output.yaml'):
        with open(yaml_filename, 'w') as outfile:
            yaml.safe_dump(self.alternativeDict, outfile, default_flow_style=False, default_style='')

    def annotate(self, fasta_filename):

        #fastaregex = re.compile(">([-|\._\w]+)\s+.+$")
        #fastaregex = re.compile(">([-\.a-zA-Z0-9_]+)\s+.+$")

        with open(fasta_filename) as fasta:
            for l in fasta:
                if l.startswith(">"):
                    res = self.fastaregex.match(l)
                    #print res.group(1)
                    if self.queryDict.has_key(res.group(1)):
                        print "{}\tBLASTORTHO\t{}\tevalue={}".format(l.rstrip(), self.queryDict[res.group(1)],
                                                         self.queryEvalueDict[res.group(1)])
                    else:
                        print "{}  NO HIT".format(l.rstrip())
                else:
                    print l.rstrip()


if __name__ == "__main__":

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hp:y:f:d:", ["pattern=", "fasta=", "dir=", "yaml="])
    except getopt.GetoptError:
        print 'fgcz_blastp_post.py -d . -p \'20160904_NCBI_Cajanus_Cajan_48522_IDs.+_[0-9]+\.json\' -f <fastafile>'
        sys.exit(2)

    fasta = None
    dir = "."
    pattern = ".+\.json"
    yaml_filename = None
    for opt, arg in opts:
        if opt == '-h':
            print "help"
            sys.exit(1)
        elif opt in ("-p", "--pattern"):
            pattern = arg
        elif opt in ("-f", "--fasta"):
            fasta = arg
            if os.path.isfile(fasta):
                pass
            else:
                print "no fasta '{}' file found.".format(fasta)
                sys.exit(1)
        elif opt in ("-d", "--dir"):
            dir = arg
        elif opt in ("-y", "--yaml"):
            yaml_filename = arg

    if fasta is None:
        print 'fasta parameter is obligatory.'
        sys.exit(1)

    app = FgczBlastp()
    app.scan(path=dir, pattern=pattern)
    app.annotate(fasta)

    if not yaml_filename is None:
        app.write_yaml(yaml_filename)
