import requests
import json

# the url we copied from browser developer tool
url = 'http://p3spectrum.ca/api/project/1/news,stage,nextStage,model,sector,leedLevel,indicator,province,subSector,refinance,tenderType,government,greenfield,(organization),governmentLevel,projectDate,projectLeed,(projectCity:city),(projectVideo:videoProvider),projectAward,projectImage,(projectRiding:politicalRiding),projectWebsite,projectSnapshot,projectProvince,projectFeatured,projectGovLevel,projectIndicator,projectGovernment,projectCoordinate,projectProcurement,projectCostBenefit,(projectParticipant:role,organization),(projectContactOrganization:contact,organization),(projectTransactionAgency:transactionAgency),(projectAdvisorCompanyRoleType:organizationType,organization,role),(projectConsortiaOrganizationRoleStage:organizationType,organization,role,consortia)'

# send http request
res = requests.get(url)

# format to dictionary
content_dict = json.loads(res.content)

# write to json file
with open("project1.json", 'w') as j_out:
    json.dump(content_dict, j_out, indent=4)