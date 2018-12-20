# Publishing on COMP

This guide describes how to publish a model on COMP. The COMP framework depends on model interfaces meeting several COMP criteria, and we walk you through how to meet those criteria, either by modifying your model's interface or building a new wrapper interface around your model. The great part is that you don't have to deal with any web technology to build your COMP app.

If you have any questions as you proceed through this guide, send Hank an email at henrymdoupe@gmail.com.

The documentation is split into three parts. The [first part](IOSCHEMA.md) documents the inputs and outputs JSON schemas that your model will need to adopt for COMP to be able to generate input forms representing your model's default specification, validate user adjustments, and display model outputs. The [second part](ENDPOINTS.md) documents the python functions that will be used by COMP to get data from and submit data to your model. The third part is a [publishing information template](TEMPLATE.md) that asks you to provide a title and overview for your new COMP app, code snippets for the three python functions, and information describing your app's resource requirements and installation directions. If you would like to see a publishing template that has already been completed, you can view the CompBaseball template [here](https://github.com/hdoupe/compbaseball/blob/master/comptemplate.md).

Once you've completed the guide, send Hank a link to the completed template -- ideally committed to your project's repository if it is public -- at henrymdoupe@gmail.com. He'll review the  information and provide guidance if any of the criteria have not been met. Then your model will be deployed to COMP. Once the model has been deployed, you will have the opportunity to test it out.

For those who are interested in a more detailed explanation of the additional steps we  take to publish your model on COMP, feel free to checkout the [Technical Publishing Guide](TECHNICALPUBLISHING.md), and, since COMP is an open-source website, you can even follow along.