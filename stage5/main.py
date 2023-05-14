import requests
import json
from os import makedirs

def project_id_to_url(project_id: int) -> str:
    return f'http://p3spectrum.ca/api/project/{project_id}/news,stage,nextStage,model,sector,leedLevel,indicator,province,subSector,refinance,tenderType,government,greenfield,(organization),governmentLevel,projectDate,projectLeed,(projectCity:city),(projectVideo:videoProvider),projectAward,projectImage,(projectRiding:politicalRiding),projectWebsite,projectSnapshot,projectProvince,projectFeatured,projectGovLevel,projectIndicator,projectGovernment,projectCoordinate,projectProcurement,projectCostBenefit,(projectParticipant:role,organization),(projectContactOrganization:contact,organization),(projectTransactionAgency:transactionAgency),(projectAdvisorCompanyRoleType:organizationType,organization,role),(projectConsortiaOrganizationRoleStage:organizationType,organization,role,consortia)'

# create a folder
makedirs("projects", exist_ok=True)

count_active = 0
project_id = 1
while True:
    url = project_id_to_url(project_id)

    # send http request
    res = requests.get(url)

    # format to dictionary
    content_dict = json.loads(res.content)

    # there's 'meta' and 'project' in content_dict
    # we want 'project'
    if 'project' in content_dict:
        project_dict = content_dict['project']

        if 'active' in project_dict and project_dict['active']:
            count_active += 1
            # write to json file
            with open(f"projects/{project_id:03d}.json", 'w') as j_out:
                json.dump(content_dict, j_out, indent=4)
            print(f"project id: {project_id} is acitve, count: {count_active}")

        # the website says there's 291 active project
        # the last active project id is 857
        if count_active >= 291:
            break
    project_id += 1