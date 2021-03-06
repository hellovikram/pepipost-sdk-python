# -*- coding: utf-8 -*-

"""
   PepipostAPIV10Lib.Models.EmailDetails
 
   This file was automatically generated by APIMATIC v2.0 on 04/15/2016
"""
from PepipostAPIV10Lib.APIHelper import APIHelper

class EmailDetails(object):

    """Implementation of the 'email_details' model.

    TODO: type model description here.

    Attributes:
        fromname (string): TODO: type description here.
        subject (string): TODO: type description here.
        mfrom (string): TODO: type description here.
        replytoid (string): TODO: type description here.
        tags (string): TODO: type description here.
        content (string): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the EmailDetails class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    fromname -- string -- Sets the attribute fromname
                    subject -- string -- Sets the attribute subject
                    from -- string -- Sets the attribute mfrom
                    replytoid -- string -- Sets the attribute replytoid
                    tags -- string -- Sets the attribute tags
                    content -- string -- Sets the attribute content
        
        """
        # Set all of the parameters to their default values
        self.fromname = None
        self.subject = None
        self.mfrom = None
        self.replytoid = None
        self.tags = None
        self.content = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "fromname": "fromname",
            "subject": "subject",
            "from": "mfrom",
            "replytoid": "replytoid",
            "tags": "tags",
            "content": "content",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

    def resolve_names(self):
        """Creates a dictionary representation of this object.
        
        This method converts an object to a dictionary that represents the
        format that the model should be in when passed into an API Request.
        Because of this, the generated dictionary may have different
        property names to that of the model itself.
        
        Returns:
            dict: The dictionary representing the object.
        
        """
        # Create a mapping from Model property names to API property names
        replace_names = {
            "fromname": "fromname",
            "subject": "subject",
            "mfrom": "from",
            "replytoid": "replytoid",
            "tags": "tags",
            "content": "content",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)