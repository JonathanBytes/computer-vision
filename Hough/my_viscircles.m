function my_viscircles(centro,radio,color)

  L=size(radio);
  for v=1:L
    for tetha=1:361
      x(tetha)=centro(v,1)+radio(v)*cosd(tetha);
      y(tetha)=centro(v,2)+radio(v)*sind(tetha);
    end
    plot(x,y,color,'LineWidth',3)
    hold on
  end

end

