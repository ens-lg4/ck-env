#
# Collective Knowledge (individual environment - setup)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin, Grigori.Fursin@cTuning.org, http://fursin.net
#

##############################################################################
# setup environment setup

import os

def setup(i):
    """
    Input:  {
              cfg              - meta of this soft entry
              self_cfg         - meta of module soft
              ck_kernel        - import CK kernel module (to reuse functions)

              host_os_uoa      - host OS UOA
              host_os_uid      - host OS UID
              host_os_dict     - host OS meta
              
              target_os_uoa    - target OS UOA
              target_os_uid    - target OS UID
              target_os_dict   - target OS meta

              target_device_id - target device ID (if via ADB)

              tags             - list of tags used to search this entry

              env              - updated environment vars from meta
              customize        - updated customize vars from meta

              deps             - resolved dependencies for this soft

              interactive      - if 'yes', can ask questions, otherwise quiet
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              bat          - prepared string for bat file
            }

    """

    import os

    # Get variables
    ck=i['ck_kernel']
    s=''

    iv=i.get('interactive','')

    env=i.get('env',{})
    cfg=i.get('cfg',{})
    deps=i.get('deps',{})
    tags=i.get('tags',[])
    cus=i.get('customize',{})

    target_d=i.get('target_os_dict',{})
    win=target_d.get('windows_base','')
    remote=target_d.get('remote','')
    mingw=target_d.get('mingw','')
    tbits=target_d.get('bits','')

    envp=cus.get('env_prefix','')
    pi=cus.get('path_install','')

    ################################################################
    if win=='yes':
       # FGG had 'Win64', however on Anton's machine it was 'x64'
       # we should check backwards compatibility in the future ...
       ext='x64'
       if os.path.isdir(pi+'\\lib\\Win64'): ext='Win64'

       if tbits=='32': ext='Win32'

       cus['path_bin']=pi+'\\bin\\'
       cus['path_lib']=pi+'\\lib\\'+ext

       cus['static_lib']='OpenCL.lib'

       cus['include_name']='CL\\opencl.h'

    else:
       x=''
       if tbits=='64': x='64'

       cus['path_bin']=pi+'/bin'
       cus['path_lib']=pi+'/lib'+x

       cus['include_name']='CL/opencl.h'

       cus['static_lib']='libOpenCL.so'
       cus['dynamic_lib']='libOpenCL.so'

    env['CK_ENV_LIB_OPENCL_INCLUDE_NAME']=cus.get('include_name','')
    env['CK_ENV_LIB_OPENCL_STATIC_NAME']=cus.get('static_lib','')
    env['CK_ENV_LIB_OPENCL_DYNAMIC_NAME']=cus.get('dynamic_lib','')

    return {'return':0, 'bat':s}
