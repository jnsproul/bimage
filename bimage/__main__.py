#! /usr/bin/env python

"""
A __main__ namespace for the bimage package.
"""
# System import
import sys
# Third party
import argparse
# Local
from .bimage import bimage


def main(argv):
    """
    Build a container image described in a GitHub repository and push that image to google cloud
    artifact registry.

    usage: bimage [-h]
                  github_org repo_name branch_or_tag local_image_name local_image_tag
                  path_to_dockerfile target_image_name target_image_tag region
                  gcloudProjectId repositoryName

    positional arguments:
      github_org          The GitHub organization of the repository
      repo_name           The name of the repository in the organization
      branch_or_tag       The branch or tag of the repository
      local_image_name    The name of the image we create locally from the Dockerfile
      local_image_tag     The tag of the image we create locally from the Dockerfile
                          (v1, 1.0.1, version2.0)
      path_to_dockerfile  The path to the docker file from the repository we cloned, usually
                          the name of the repository
      target_image_name   The target image name, i.e. the name of the image we store in the
                          google cloud artifact registry
      target_image_tag    The target image tag, i.e. the tag of the image we store in the
                          google cloud artifact registry (v1,
                          1.0.1, version2.0)
      region              Region the image will be stored in the google cloud
                          (e.g. us-east1, us, eu)
      gcloudProjectId     The project id from which the image will be stored under in a
                          google artifact registry
      repositoryName      The name of the google cloud artifact registry that holds docker images

    options:
        -h, --help     show help message and exit

    example:
        $ python bimage cbcunc timage develop testimage v1 timage testimage v1\
            us-east1 bimage-project bimage-repository
    """

    parser = argparse.ArgumentParser(prog='bimage',
                                     description='Build a container image described in a \
                                        GitHub repository and push that image to google \
                                            cloud artifact registry.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("github_org",
                        help="The GitHub organization of the repository")
    parser.add_argument("repo_name",
                        help="The name of the repository in the organization")
    parser.add_argument("branch_or_tag",
                        help="The branch or tag of the repository")
    parser.add_argument("local_image_name",
                        help="The name of the image we create locally from the Dockerfile")
    parser.add_argument("local_image_tag",
                        help="The tag of the image we create locally from the Dockerfile \
                            (v1, 1.0.1, version2.0)")
    parser.add_argument("path_to_dockerfile",
                        help="The path to the docker file from the repository we cloned, \
                            usually the name of the repository")
    parser.add_argument("target_image_name",
                        help="The target image name, i.e. the name of the image we store \
                            in the google cloud artifact registry")
    parser.add_argument("target_image_tag",
                        help="The target image tag, i.e. the tag of the image we store in \
                            the google cloud artifact registry (v1, 1.0.1, version2.0)")
    parser.add_argument("region",
                        help="Region the image will be stored in the google cloud (e.g. \
                            us-east1, us, eu)")
    parser.add_argument("gcloudProjectId",
                        help="The project id from which the image will be stored under in \
                            a google artifact registry")
    parser.add_argument("repositoryName",
                        help="The name of the google cloud artifact registry that holds \
                            docker images")
    args = parser.parse_args(argv)
    bimage(args.github_org, args.repo_name, args.branch_or_tag,
           args.local_image_name, args.local_image_tag,
           args.path_to_dockerfile, args.target_image_name,
           args.target_image_tag, args.region, args.gcloudProjectId,
           args.repositoryName)


if __name__ == '__main__':
    main(sys.argv[1:])
