import boto3
import botocore
import json
import config
import res.utils as utils
import res.glob  as glob

# =======================================================================================================================
#
#  Supported services   : Directory Service 
#  Unsupported services : Cognito, Secrets Manager, GuardDuty, Inspector, Amazon Macie, AWS Single Sign-On, Certificate Manager, CloudHSM, 
#                           WAF & Shield, Artifact
#
#  Note: IAM has its own module
#
# =======================================================================================================================

#  ------------------------------------------------------------------------
#
#    Cloud Directory (simple)
#
#  ------------------------------------------------------------------------

def get_clouddirectory_inventory(oId):
    """
        Returns keys managed by KMS (global)

        :param oId: ownerId (AWS account)
        :type oId: string

        :return: clouddirectory inventory
        :rtype: json

        ..note:: http://boto3.readthedocs.io/en/latest/reference/services/clouddirectory.html
    """ 
    return glob.get_inventory(
        ownerId = oId,
        aws_service = "clouddirectory", 
        aws_region = "all", 
        function_name = "list_directories", 
        key_get = "Directories"
    )


#  ------------------------------------------------------------------------
#
#    ACM (Certificate Manager)
#
#  ------------------------------------------------------------------------

def get_acm_inventory(oId):
    """
        Returns certificates managed with ACM

        :param oId: ownerId (AWS account)
        :type oId: string

        :return: certificates inventory
        :rtype: json

        ..note:: https://boto3.readthedocs.io/en/latest/reference/services/acm.htm
    """ 
    return glob.get_inventory(
        ownerId = oId,
        aws_service = "acm", 
        aws_region = "all", 
        function_name = "list_certificates", 
        key_get = "CertificateSummaryList",
        detail_function = "describe_certificate", 
        join_key = "CertificateArn", 
        detail_join_key = "CertificateArn", 
        detail_get_key = "Certificate"        
    )


#  ------------------------------------------------------------------------
#
#    ACMPCA (Certificate Manager Private Certificate Authority). Not implemented yet.
#
#  ------------------------------------------------------------------------

def get_acmpca_inventory(oId):
    """
        Returns certificates managed with ACM

        :param oId: ownerId (AWS account)
        :type oId: string

        :return: certificates inventory
        :rtype: json

        ..note:: https://boto3.readthedocs.io/en/latest/reference/services/acm-pca.html
    """ 
    return glob.get_inventory(
        ownerId = oId,
        aws_service = "acm-pca", 
        aws_region = "all", 
        function_name = "list_certificate_authorities", 
        key_get = "CertificateAuthorities" 
    )


#
# Hey, doc: we're in a module!
#
if (__name__ == '__main__'):
    print('Module => Do not execute')