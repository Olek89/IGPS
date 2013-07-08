surf(b04103f40x2D68900x2D421c0x2D86a30x2D2f787c4ba5ae_result,'DisplayName','b04103f40x2D68900x2D421c0x2D86a30x2D2f787c4ba5ae_result');figure(gcf)

set(gca,'XTickLabel',{'-150','-100','-50','0','50','100','150'})
set(gca,'XTick',0:50:300)
set(gca,'YTickLabel',{'-150','-100','-50','0','50','100','150'})
set(gca,'YTick',0:50:300)

xLabel('position in x axis in respect to home [m]')
yLabel('position in y axis in respect to home [m]')
zLabel('presence probability')
title('Example simulation result for 3 active nodes')

view([-35,-60,170]);